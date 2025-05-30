import os
import random
import requests
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse,Http404
from django.db.models.signals import post_save
from django.dispatch import receiver
from .forms import SignupForm
from django.views.decorators.csrf import csrf_exempt    
from dotenv import load_dotenv
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Song,Artist,Favorites, Playlist, User,UserType,Album,Listen
from .forms import LoginForm
from django.contrib.auth.hashers import check_password 
from django.utils.timezone import now
import logging
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect, get_object_or_404
from .models import SongRequest, Song, Album, Artist, Genre, ArtistFollow
from .utils import upload_to_pcloud
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from datetime import date
from tinytag import TinyTag
from django.db import transaction
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank

# Load environment variables
load_dotenv()
logger = logging.getLogger(__name__)

# Fetch credentials from environment variables
PCLOUD_USERNAME = os.getenv('PCLOUD_USERNAME')
PCLOUD_PASSWORD = os.getenv('PCLOUD_PASSWORD')
PCLOUD_MUSIC_FOLDER = os.getenv('PCLOUD_MUSIC_FOLDER')

# Signup view
def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been created successfully!")
            return redirect('login')
        else:
            messages.error(request, "Signup failed. Please fix the errors below.")
    else:
        form = SignupForm()

    user_types = UserType.objects.all()  # Fetch all user types for dropdown
    return render(request, 'signup2.html', {'form': form, 'user_types': user_types})

# Login view
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            try:
                user = User.objects.get(email=email)
                if check_password(password, user.password):  # Verify hashed password
                    login(request, user)  # Log the user in
                    messages.success(request, "You have successfully logged in!")
                    return redirect('index')  # Redirect to a success page
                else:
                    messages.error(request, "Invalid email or password.")
            except User.DoesNotExist:
                messages.error(request, "User with this email does not exist.")
        else:
            messages.error(request, "Invalid form submission.")
    else:
        form = LoginForm()

    return render(request, 'login2.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully!")
    return redirect('login')

# Index view (Home page)
def index(request):
    return render(request, 'index2.html')  # Assuming index.html is the homepage of your app

@login_required
def profile_view(request):
    return render(request, 'account.html')

@login_required
def edit_profile(request):
    user = request.user

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user.gender = request.POST.get('gender')
        user.country = request.POST.get('country')
        user.date_of_birth = request.POST.get('date_of_birth')

        user.name = name
        user.email = email

        if password:
            user.password = make_password(password)

        user.save()
        messages.success(request, "Profile updated successfully!")
        return redirect('profile_view')

    return render(request, 'edit_profile.html')

@login_required
def request_song(request):
    if request.method == "POST":
        song_title = request.POST.get('song_title')
        album = request.POST.get('album')
        artist = request.POST.get('artist')
        genre = request.POST.get('genre')
        release_year = request.POST.get('release_year')

        SongRequest.objects.create(
            user=request.user,
            admin=User.objects.filter(user_type__user_type_name='Admin').first(),
            song_title=song_title,
            album=album,
            artist=artist,
            genre=genre,
            release_year=release_year,
            status="Pending",
        )
        messages.success(request, "🎵 Your song request has been submitted successfully!")
        return redirect('request_song')  # Reload the same page to see the new request

    # ✅ Fetch all requests by this user to display below the form
    my_requests = SongRequest.objects.filter(user=request.user).order_by('-request_date')

    return render(request, 'request_song.html', {'my_requests': my_requests})

@login_required
def admin_view_song_requests(request):
    if request.user.user_type.user_type_name != "Admin":
        return redirect('index')  # Not allowed if not Admin

    song_requests = SongRequest.objects.all().order_by('-request_date')
    return render(request, 'admin_view_song_requests.html', {'song_requests': song_requests})


@login_required
def admin_upload_song(request, id):
    song_request = get_object_or_404(SongRequest, id=id)

    if request.method == 'POST':
        mp3_file = request.FILES['mp3_file']

        if mp3_file:
            # Set the file storage path
            file_storage = FileSystemStorage(location=settings.MEDIA_ROOT)
            
            # Save the file to the defined MEDIA_ROOT directory
            filename = file_storage.save(mp3_file.name, mp3_file)
            file_url = file_storage.url(filename)  # Get the URL of the file

            # Debugging: Check if the file is saved
            print(f"File uploaded and saved as: {filename}")
            print(f"File is accessible at: {file_url}")

            # Now upload the file to pCloud
            # Pass the mp3_file directly instead of the filename string
            file_url_pcloud = upload_to_pcloud(mp3_file)

            if file_url_pcloud:
                # Update SongRequest status to 'Approved' after successful upload
                song_request.status = 'Approved'  # Update status to 'Approved'
                song_request.file_url = file_url_pcloud  # Save the pCloud URL
                song_request.save()  # Save the changes

                messages.success(request, "Song uploaded successfully and uploaded to pCloud.")
                return redirect('admin_view_song_requests')
            else:
                messages.error(request, "Failed to upload to pCloud.")
                return redirect('admin_view_song_requests')
        else:
            messages.error(request, "No MP3 file uploaded.")
            return redirect('admin_view_song_requests')


@login_required
def reject_song_request(request, id):
    song_request = get_object_or_404(SongRequest, id=id)

    if request.method == 'POST':
        song_request.status = 'Rejected'
        song_request.save()
        messages.success(request, "Song request rejected.")
        return redirect('admin_view_song_requests')


@login_required
def upload_song(request):
    if request.method == 'POST':
        song_title = request.POST['song_title']
        artist_name = request.POST['artist']
        album_name = request.POST['album']
        genre_name = request.POST['genre']
        release_date = request.POST['release_date']  # This will be in the format YYYY-MM-DD
        mp3_file = request.FILES['mp3_file']

        # Parse the release date into a date object
        try:
            release_date = date.fromisoformat(release_date)
        except ValueError:
            messages.error(request, "Invalid release date.")
            return redirect('upload_song')

        # Check if the artist exists, if not, create it
        artist, created = Artist.objects.get_or_create(name=artist_name)

        # Check if the genre exists, if not, create it
        genre, created = Genre.objects.get_or_create(name=genre_name)

        # Try to get the album based on title and artist
        album = Album.objects.filter(title=album_name, artist=artist).first()

        if not album:
            # If the album doesn't exist, create a new one with the release_date
            album = Album.objects.create(
                title=album_name,
                artist=artist,
                release_date=release_date  # Use the parsed release_date
            )

        # Handle file saving
        fs = FileSystemStorage()
        filename = fs.save(mp3_file.name, mp3_file)
        file_url = fs.url(filename)

        # Extract the duration of the MP3 file using TinyTag
        tag = TinyTag.get(f'./media/{filename}')
        duration = int(tag.duration)  # Get the duration in seconds

        # Get the current logged-in user (admin)
        admin_user = request.user

        # Create the song entry, with the admin field populated and the duration
        song = Song.objects.create(
            title=song_title,
            album=album,
            artist=artist,
            genre=genre,
            released_year=release_date.year,
            released_month=release_date.month,
            released_day=release_date.day,
            duration=duration,  # Save the duration (in seconds)
            file_url=file_url,  # Save the file URL
            admin=admin_user  # Set the admin to the logged-in user
        )

        messages.success(request, "Song uploaded successfully!")
        return redirect('song_list')

    return render(request, 'upload_song.html')

# Admin Dashboard View
@login_required
def admin_dashboard(request):
    # Fetch totals for songs, artists, albums, and genres
    total_songs = Song.objects.count()
    total_artists = Artist.objects.count()
    total_albums = Album.objects.count()
    total_genres = Genre.objects.count()

    # Check if the user is an admin
    is_admin = request.user.is_superuser

    context = {
        'total_songs': total_songs,
        'total_artists': total_artists,
        'total_albums': total_albums,
        'total_genres': total_genres,
        'is_admin': is_admin
    }
    return render(request, 'admin_dashboard.html', context)

# View all songs
@login_required
def view_songs(request):
    songs = Song.objects.all()
    return render(request, 'song_list_detail.html', {'songs': songs})

@login_required
def view_artists(request):
    artists = Artist.objects.all()
    artist_data = []
    
    for artist in artists:
        is_followed = ArtistFollow.objects.filter(user=request.user, artist=artist).exists()
        artist_data.append({
            'name': artist.name,
            'bio': artist.bio,
            'followers': artist.followers,
            'genre': artist.genre.name,
            'streams': artist.streams,
            'songs': artist.song_set.all(),
            'albums': artist.album_set.all(),
            'is_followed': is_followed  # Pass the flag to the template
        })
    
    return render(request, 'artist_list.html', {'artists': artist_data})



# View all albums with their genres, artists, and songs
@login_required
def view_albums(request):
    albums = Album.objects.all()
    album_data = []
    for album in albums:
        total_streams = sum(song.streams for song in album.song_set.all())  # Sum streams of all songs in the album
        album_data.append({
            'title': album.title,
            'release_date': album.release_date,
            'artist': album.artist.name,
            'songs': album.song_set.all(),
            'total_streams': total_streams,  # Add total streams to album data
        })

    return render(request, 'album_list.html', {'albums': album_data})

# View all genres with their artists, albums, and songs
@login_required
def view_genres(request):
    genres = Genre.objects.all()
    genre_data = []
    
    for genre in genres:
        # Get unique artists for each genre using distinct
        artists = genre.artist_set.all().distinct()

        # Calculate total streams for the genre by summing up the streams of each song in the genre
        total_streams = sum(song.streams for song in genre.song_set.all())

        genre_data.append({
            'name': genre.name,
            'artists': artists,
            'songs': genre.song_set.all(),
            'total_streams': total_streams,
        })

    return render(request, 'genres_list.html', {'genres': genre_data})



# View all songs
@login_required
def view_songs(request):
    songs = Song.objects.all()  # Fetch all songs
    return render(request, 'song_list_detail.html', {'songs': songs})


# Song detailsimport logging

# Create a logger
logger = logging.getLogger(__name__)

# Set the logging level
logger.setLevel(logging.DEBUG)

# Create a file handler
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.DEBUG)

# Create a console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Create a formatter and set it for the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Add logs to the existing code
def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            logger.info("User signed up successfully")
            messages.success(request, "Your account has been created successfully!")
            return redirect('login')
        else:
            logger.error("Signup failed")
            messages.error(request, "Signup failed. Please fix the errors below.")
    else:
        form = SignupForm()

    user_types = UserType.objects.all()  # Fetch all user types for dropdown
    return render(request, 'signup2.html', {'form': form, 'user_types': user_types})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            try:
                user = User.objects.get(email=email)
                if check_password(password, user.password):  # Verify hashed password
                    logger.info("User logged in successfully")
                    login(request, user)  # Log the user in
                    messages.success(request, "You have successfully logged in!")
                    return redirect('index')  # Redirect to a success page
                else:
                    logger.error("Invalid email or password")
                    messages.error(request, "Invalid email or password.")
            except User.DoesNotExist:
                logger.error("User does not exist")
                messages.error(request, "User with this email does not exist.")
        else:
            logger.error("Invalid form submission")
            messages.error(request, "Invalid form submission.")
    else:
        form = LoginForm()

    return render(request, 'login2.html', {'form': form})

def logout_view(request):
    logger.info("User logged out successfully")
    logout(request)
    messages.success(request, "You have been logged out successfully!")
    return redirect('login')

def index(request):
    logger.info("User accessed the index page")
    return render(request, 'index2.html')  # Assuming index.html is the homepage of your app

def profile_view(request):
    logger.info("User accessed the profile page")
    return render(request, 'account.html')

def edit_profile(request):
    user = request.user

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user.gender = request.POST.get('gender')
        user.country = request.POST.get('country')
        user.date_of_birth = request.POST.get('date_of_birth')

        user.name = name
        user.email = email

        if password:
            user.password = make_password(password)

        user.save()
        logger.info("User profile updated successfully")
        messages.success(request, "Profile updated successfully!")
        return redirect('profile_view')

    return render(request, 'edit_profile.html')

def request_song(request):
    if request.method == "POST":
        song_title = request.POST.get('song_title')
        album = request.POST.get('album')
        artist = request.POST.get('artist')
        genre = request.POST.get('genre')
        release_year = request.POST.get('release_year')

        SongRequest.objects.create(
            user=request.user,
            admin=User.objects.filter(user_type__user_type_name='Admin').first(),
            song_title=song_title,
            album=album,
            artist=artist,
            genre=genre,
            release_year=release_year,
            status="Pending",
        )
        logger.info("Song request submitted successfully")
        messages.success(request, "Your song request has been submitted successfully!")
        return redirect('request_song')  # Reload the same page to see the new request

    # Fetch all requests by this user to display below the form
    my_requests = SongRequest.objects.filter(user=request.user).order_by('-request_date')

    return render(request, 'request_song.html', {'my_requests': my_requests})

def admin_view_song_requests(request):
    if request.user.user_type.user_type_name != "Admin":
        logger.error("Unauthorized access to admin view song requests")
        return redirect('index')  # Not allowed if not Admin

    song_requests = SongRequest.objects.all().order_by('-request_date')
    logger.info("Admin viewed song requests successfully")
    return render(request, 'admin_view_song_requests.html', {'song_requests': song_requests})

def admin_upload_song(request, id):
    song_request = get_object_or_404(SongRequest, id=id)

    if request.method == 'POST':
        mp3_file = request.FILES['mp3_file']

        if mp3_file:
            # Set the file storage path
            file_storage = FileSystemStorage(location=settings.MEDIA_ROOT)
            
            # Save the file to the defined MEDIA_ROOT directory
            filename = file_storage.save(mp3_file.name, mp3_file)
            file_url = file_storage.url(filename)  # Get the URL of the file

            # Debugging: Check if the file is saved
            print(f"File uploaded and saved as: {filename}")
            print(f"File is accessible at: {file_url}")

            # Now upload the file to pCloud
            # Pass the mp3_file directly instead of the filename string
            file_url_pcloud = upload_to_pcloud(mp3_file)

            if file_url_pcloud:
                # Update SongRequest status to 'Approved' after successful upload
                song_request.status = 'Approved'  # Update status to 'Approved'
                song_request.file_url = file_url_pcloud  # Save the pCloud URL
                song_request.save()  # Save the changes

                logger.info("Song uploaded successfully and uploaded to pCloud")
                messages.success(request, "Song uploaded successfully and uploaded to pCloud.")
                return redirect('admin_view_song_requests')
            else:
                logger.error("Failed to upload to pCloud")
                messages.error(request, "Failed to upload to pCloud.")
                return redirect('admin_view_song_requests')
        else:
            logger.error("No MP3 file uploaded")
            messages.error(request, "No MP3 file uploaded.")
            return redirect('admin_view_song_requests')

def reject_song_request(request, id):
    song_request = get_object_or_404(SongRequest, id=id)

    if request.method == 'POST':
        song_request.status = 'Rejected'
        song_request.save()
        logger.info("Song request rejected successfully")
        messages.success(request, "Song request rejected.")
        return redirect('admin_view_song_requests')

def upload_song(request):
    if request.method == 'POST':
        song_title = request.POST['song_title']
        artist_name = request.POST['artist']
        album_name = request.POST['album']
        genre_name = request.POST['genre']
        release_date = request.POST['release_date']  # This will be in the format YYYY-MM-DD
        mp3_file = request.FILES['mp3_file']

        # Parse the release date into a date object
        try:
            release_date = date.fromisoformat(release_date)
        except ValueError:
            logger.error("Invalid release date")
            messages.error(request, "Invalid release date.")
            return redirect('upload_song')

        # Check if the artist exists, if not, create it
        artist, created = Artist.objects.get_or_create(name=artist_name)

        # Check if the genre exists, if not, create it
        genre, created = Genre.objects.get_or_create(name=genre_name)

        # Try to get the album based on title and artist
        album = Album.objects.filter(title=album_name, artist=artist).first()

        if not album:
            # If the album doesn't exist, create a new one with the release_date
            album = Album.objects.create(
                title=album_name,
                artist=artist,
                release_date=release_date  # Use the parsed release_date
            )

        # Handle file saving
        fs = FileSystemStorage()
        filename = fs.save(mp3_file.name, mp3_file)
        file_url = fs.url(filename)

        # Extract the duration of the MP3 file using TinyTag
        tag = TinyTag.get(f'./media/{filename}')
        duration = int(tag.duration)  # Get the duration in seconds

        # Get the current logged-in user (admin)
        admin_user = request.user

        # Create the song entry, with the admin field populated and the duration
        song = Song.objects.create(
            title=song_title,
            album=album,
            artist=artist,
            genre=genre,
            released_year=release_date.year,
            released_month=release_date.month,
            released_day=release_date.day,
            duration=duration,  # Save the duration (in seconds)
            file_url=file_url,  # Save the file URL
            admin=admin_user  # Set the admin to the logged-in user
        )

        logger.info("Song uploaded successfully")
        messages.success(request, "Song uploaded successfully!")
        return redirect('song_list')

    return render(request, 'upload_song.html')

def admin_dashboard(request):
    # Fetch totals for songs, artists, albums, and genres
    total_songs = Song.objects.count()
    total_artists = Artist.objects.count()
    total_albums = Album.objects.count()
    total_genres = Genre.objects.count
@login_required
def song_detail(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    return render(request, 'song_list_detail.html', {'song': song})

# Increment song streams (for "Now Playing")
@login_required
def increment_stream(request, song_id):
    try:
        song = Song.objects.get(id=song_id)
        song.streams += 1
        song.save()
        return JsonResponse({"success": True, "streams": song.streams})
    except Song.DoesNotExist:
        return JsonResponse({"error": "Song not found"}, status=404)
    
# Edit Song View
@login_required
def edit_song(request, song_id):
    song = get_object_or_404(Song, id=song_id)

    if request.method == 'POST':
        # Save the form data to the song instance
        song.title = request.POST['title']
        song.artist.name = request.POST['artist']
        song.album.title = request.POST['album']
        song.genre.name = request.POST['genre']
        song.released_year = request.POST['released_year']
        song.duration = request.POST['duration']
        
        # Save the updated song to the database
        song.save()
        song.artist.save()  # Save artist if changes were made
        song.album.save()   # Save album if changes were made
        song.genre.save()   # Save genre if changes were made
        
        return redirect('view_songs')  # Redirect to the songs list page

    # Render the edit song form if it's a GET request
    return render(request, 'edit_song.html', {'song': song})

# Delete Song View
@login_required
def delete_song(request, song_id):
    song = get_object_or_404(Song, id=song_id)

    # Delete the song
    song.delete()

    # Redirect to the songs list after deletion
    return redirect('view_songs')

@login_required
def artist_list(request):
    artists = Artist.objects.all()
    followed_ids = ArtistFollow.objects.filter(user=request.user).values_list('artist_id', flat=True)
    for artist in artists:
        artist.is_followed = artist.id in followed_ids
    return render(request, 'artist_list.html', {'artists': artists})

@login_required
def follow_artist(request, artist_id):
    if request.method == 'POST':
        artist = get_object_or_404(Artist, id=artist_id)
        ArtistFollow.objects.get_or_create(user=request.user, artist=artist)
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'message': 'Invalid request'}, status=400)

@login_required
def unfollow_artist(request, artist_id):
    if request.method == 'POST':
        artist = get_object_or_404(Artist, id=artist_id)
        ArtistFollow.objects.filter(user=request.user, artist=artist).delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'message': 'Invalid request'}, status=400)

@login_required
def followed_artists(request):
    followed = ArtistFollow.objects.filter(user=request.user).select_related('artist')
    followed_artists = [f.artist for f in followed]
    return render(request, 'followed_artists.html', {'followed_artists': followed_artists})

# Authenticate with pCloud
def authenticate_pcloud():
    response = requests.post(
        'https://api.pcloud.com/login',
        data={'username': PCLOUD_USERNAME, 'password': PCLOUD_PASSWORD}
    )
    data = response.json()
    if 'auth' in data:
        return data['auth']
    else:
        raise Exception(f"Authentication failed: {data.get('error', 'Unknown error')}")

# List contents of the specified folder
def list_folder_contents(auth_token, folder_path):
    response = requests.post(
        'https://api.pcloud.com/listfolder',
        data={'auth': auth_token, 'path': folder_path}
    )
    return response.json()

def song_list(request):
    try:
        # Fetch songs from the database, including the artist's name
        db_songs = Song.objects.all().select_related('artist').values('title', 'file_url', 'artist__name','id')

        # Fetch songs from pCloud
        auth_token = authenticate_pcloud()
        folder_contents = list_folder_contents(auth_token, PCLOUD_MUSIC_FOLDER)
        pcloud_songs = [
            {"name": item["name"], "path": item["path"]}
            for item in folder_contents.get("metadata", {}).get("contents", [])
            if not item["isfolder"]
        ]

        # Combine database and pCloud songs
        songs = []
        for song in db_songs:
            title_with_extension = f"{song['title']}.mp3"
            matching_pcloud_song = next(
                (psong for psong in pcloud_songs if psong['name'] == title_with_extension),
                None
            )
            if matching_pcloud_song:
                songs.append({
                    "title": song['title'],
                    "file_url": matching_pcloud_song['path'],
                    "artist": song['artist__name'], # Get artist's name directly
                    "id": song['id']
                })
            else:
                songs.append({
                    "title": song['title'],
                    "file_url": song['file_url'],  # In case no pCloud match
                    "artist": song['artist__name'],
                    "id": song['id']
                })

        return render(request, "index2.html", {"songs": songs})

    except Exception as e:
        return HttpResponse(f"Error: {str(e)}", status=500)


def search(request):
    query = request.POST.get('search_query', '').strip()  # Use POST for form submission
    if query:
        # Create search vector for songs' title and artists' names
        search_vector = (
            SearchVector('title', weight='A') +  # Search songs by title
            SearchVector('artist__name', weight='B')  # Search artists by name
        )
        search_query = SearchQuery(query)

        # Search songs and rank them
        songs = (
            Song.objects.annotate(rank=SearchRank(search_vector, search_query))
            .filter(rank__gte=0.1)  # Filter by relevance
            .order_by('-rank')
        )

        # Search for artists
        artists = Artist.objects.annotate(search=SearchVector('name')).filter(search=search_query)
    else:
        # If no query is provided, return empty lists
        songs, artists = [], []

    # Prepare context
    context = {
        'query': query,
        'songs': songs,
        'artists': artists,
        'search_results_count': len(songs) + len(artists),  # Total number of results
    }
    return render(request, 'search.html', context)


# use this play_song to play the clcking song in the now playing songs part 
def play_song(request, song_title):
    """Fetch the song, increment the stream count, and return the playback URL."""
    try:
        # Fetch song from database
        song = Song.objects.filter(title=song_title).first()
        if not song:
            return JsonResponse({"error": "Song found in database."}, status=404)

        # Authenticate with pCloud
        auth_token = authenticate_pcloud()

        # Fetch file path from pCloud
        folder_contents = list_folder_contents(auth_token, PCLOUD_MUSIC_FOLDER)
        matching_song = next(
            (item for item in folder_contents.get("metadata", {}).get("contents", [])
             if not item["isfolder"] and item["name"] == f"{song_title}.mp3"),
            None
        )

        if not matching_song:
            return JsonResponse({"error": "Song not found in pCloud."}, status=404)

        # Get file link
        file_path = matching_song["path"]
        response = requests.post(
            'https://api.pcloud.com/getfilelink',
            data={'auth': auth_token, 'path': file_path}
        )
        if response.status_code != 200:
            return HttpResponse("Error fetching song link.", status=400)

        file_link = f"https://{response.json()['hosts'][0]}{response.json()['path']}"

        # Create a Listen record (triggers the increment in the database)
        Listen.objects.create(
            user=request.user,
            song=song,
            played_at=now(),
            status='played',
            play_mode='online',
        )
        
           # Log stream count increment
        song.refresh_from_db()  # Fetch updated song object after the trigger executes
        logger.info(f"Song '{song.title}' streams incremented to: {song.streams}")
        print("stream is +1")

        # Return the song URL
        return JsonResponse({"url": file_link})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

def song_detail(request, song_index):
    songs = Song.objects.all()
    song = songs[song_index]  # Assuming `Song` is your model and `song_index` is passed
    return render(request, 'song_detail.html', {
        'songs': songs,
        'song': song,
        'song_index': song_index
    })
    
    

@login_required
def add_to_favorites(request, song_id):
    if request.method == 'POST':
        try:
            user = request.user
            song = Song.objects.get(id=song_id)

            # Check if the song is already in the user's favorites
            if Favorites.objects.filter(user=user, song=song).exists():
                return JsonResponse({'error': 'Song is already in favorites.'}, status=400)

            # Add the song to favorites
            favorite = Favorites.objects.create(
                user=user,
                song=song,
                album=song.album,
                artist=song.artist
            )
            favorite.save()
            return JsonResponse({'message': 'Song added to favorites!'})
        except Song.DoesNotExist:
            return JsonResponse({'error': 'Song does not exist.'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method.'}, status=400)


@login_required
def remove_from_favorites(request, song_id):
    if request.method == 'POST':
        try:
            favorite = Favorites.objects.get(user=request.user, song__id=song_id)
            favorite.delete()
            return JsonResponse({'message': 'Song removed from favorites!'})
        except Favorites.DoesNotExist:
            return JsonResponse({'error': 'Favorite not found.'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method.'}, status=400)
@login_required
def my_music(request):

    user = request.user
    listens = Listen.objects.filter(user=user).order_by('-played_at')
    
    # Remove duplicate songs manually
    unique_songs = {}
    for listen in listens:
        if listen.song.id not in unique_songs:
            unique_songs[listen.song.id] = listen
    
    # Convert to a list
    unique_listens = list(unique_songs.values())
    
    return render(request, 'my_music.html', {'listens': unique_listens})


@login_required
def favorites(request):
    user = request.user
    favorites = Favorites.objects.filter(user=user).select_related('song', 'album', 'artist')
    return render(request, 'favorites.html', {'favorites': favorites})
@login_required
def show_artists(request):
    user = request.user
    
    # Get all listens by the user, ordered by most recent
    listens = Listen.objects.filter(user=user).order_by('-played_at')

    # Remove duplicate songs manually by storing the first occurrence in a dictionary
    unique_songs = {}
    for listen in listens:
        if listen.song.id not in unique_songs:
            unique_songs[listen.song.id] = listen

    # Get the unique listens as a list
    unique_listens = list(unique_songs.values())

    # Get a list of artists based on the unique songs
    artist_ids = set([listen.song.artist.id for listen in unique_listens])

    # Get artist objects from the artist ids
    artists = Artist.objects.filter(id__in=artist_ids)

    # Pass the artists to the template
    return render(request, 'artists.html', {'artists': artists})

@login_required
def get_artist_songs(request, artist_id):
    try:
        user = request.user
        
        # Get all listens by the user, ordered by most recent
        listens = Listen.objects.filter(user=user).order_by('-played_at')

        # Remove duplicate songs manually by storing the first occurrence in a dictionary
        unique_songs = {}
        for listen in listens:
            if listen.song.id not in unique_songs:
                unique_songs[listen.song.id] = listen

        # Get the unique listens as a list
        unique_listens = list(unique_songs.values())

        # Get the artist by id
        artist = Artist.objects.get(id=artist_id)

        # Filter unique listens to only include songs from the requested artist
        artist_songs = []
        for listen in unique_listens:
            if listen.song.artist.id == artist.id:  # Check if the song's artist matches the requested artist
                artist_songs.append({
                    'song_id': listen.song.id,
                    'song_title': listen.song.title,
                    'artist_name': listen.song.artist.name,
                })

        return JsonResponse({"songs": artist_songs})

    except Artist.DoesNotExist:
        return JsonResponse({"error": "Artist not found."}, status=404)
@login_required
def show_album(request):
    user = request.user
    
    # Get all listens by the user, ordered by most recent
    listens = Listen.objects.filter(user=user).order_by('-played_at')

    # Remove duplicate songs manually by storing the first occurrence in a dictionary
    unique_songs = {}
    for listen in listens:
        if listen.song.id not in unique_songs:
            unique_songs[listen.song.id] = listen

    # Get the unique listens as a list
    unique_listens = list(unique_songs.values())

    # Get the albums which contain songs that the user has listened to
    album_ids = set([listen.song.album.id for listen in unique_listens if listen.song.album])
    albums = Album.objects.filter(id__in=album_ids)

    return render(request, 'album.html', {'albums': albums})

@login_required
def get_album_songs(request, album_id):
    try:
        user = request.user
        
        # Get all listens by the user, ordered by most recent
        listens = Listen.objects.filter(user=user).order_by('-played_at')

        # Remove duplicate songs manually by storing the first occurrence in a dictionary
        unique_songs = {}
        for listen in listens:
            if listen.song.id not in unique_songs:
                unique_songs[listen.song.id] = listen

        # Get the unique listens as a list
        unique_listens = list(unique_songs.values())

        # Get the album by id
        album = Album.objects.get(id=album_id)

        # Filter unique listens to only include songs from the requested album
        album_songs = []
        for listen in unique_listens:
            if listen.song.album.id == album.id:  # Check if the song's album matches the requested album
                album_songs.append({
                    'song_id': listen.song.id,
                    'song_title': listen.song.title,
                    'artist_name': listen.song.artist.name,
                })

        return JsonResponse({"songs": album_songs})

    except Album.DoesNotExist:
        return JsonResponse({"error": "Album not found."}, status=404)


@login_required
def top_songs(request):
    top_songs = Song.objects.select_related('artist').order_by('-streams')[:5]
    print("Top Songs:", top_songs)
    # return render(request, 'index2.html', {'top_songs': top_songs})
    return JsonResponse({"songs": top_songs})
@login_required
def top_songs(request):
    top_songs = Song.objects.select_related('artist').order_by('-streams')[:5]
    songs_data = [
        {
            "song_id": song.id,
            "song_title": song.title,
            "artist_name": song.artist.name,
            "streams": song.streams,
        }
        for song in top_songs
    ]
    return JsonResponse({"songs": songs_data})

def increment_stream(request, song_id):
    try:
        song = Song.objects.get(id=song_id)
        song.streams += 1
        song.save()
        return JsonResponse({"success": True, "streams": song.streams})
    except Song.DoesNotExist:
        return JsonResponse({"error": "Song not found"})
    
@login_required   
def shuffled_songs_view(request):
    shuffled_songs = Song.objects.order_by('?')  # Efficient random ordering
    return render(request, 'index2.html', {'songs': shuffled_songs})

@login_required
def shuffled_my_songs_view(request):
    user = request.user
    listens = Listen.objects.filter(user=user).order_by('-played_at')

    # Remove duplicate songs
    unique_songs = {}
    for listen in listens:
        if listen.song.id not in unique_songs:
            unique_songs[listen.song.id] = listen

    # Convert to list and shuffle
    unique_listens = list(unique_songs.values())
    random.shuffle(unique_listens)

    return render(request, 'my_music.html', {'listens': unique_listens})