import os
import requests
from django.shortcuts import render, redirect
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


# Search view   
def search(request):
    query = request.GET.get('q', '').strip()  # Get and clean the query
    if query:  # Only perform the search if a query is provided
        search_vector = (
            SearchVector('title', weight='A') +
            SearchVector('artist__name', weight='B') +
            SearchVector('genre__name', weight='C')
        )
        search_query = SearchQuery(query)

        # Search songs with ranking
        songs = (
            Song.objects.annotate(rank=SearchRank(search_vector, search_query))
            .filter(rank__gte=0.1)  # Filter by relevance
            .order_by('-rank')
        )

        # Search artists, albums, and playlists (simplified search for these models)
        artists = Artist.objects.annotate(search=SearchVector('name')).filter(search=search_query)
        albums = Album.objects.annotate(search=SearchVector('title')).filter(search=search_query)
        playlists = Playlist.objects.annotate(search=SearchVector('name')).filter(search=search_query)
    else:
        # Empty query, return empty lists
        songs, artists, albums, playlists = [], [], [], []

    context = {
        'query': query,
        'songs': songs,
        'artists': artists,
        'albums': albums,
        'playlists': playlists,
    }
    return render(request, 'music/search_results.html', context)          
# use this play_song to play the clcking song in the now playing songs part 
def play_song(request, song_title):
    """Fetch the song, increment the stream count, and return the playback URL."""
    try:
        # Fetch song from database
        song = Song.objects.filter(title=song_title).first()
        if not song:
            return JsonResponse({"error": "Song not found in database."}, status=404)

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