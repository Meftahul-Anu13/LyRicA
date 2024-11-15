import os
import requests
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from .forms import SignupForm
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Fetch credentials from environment variables
PCLOUD_USERNAME = os.getenv('PCLOUD_USERNAME')
PCLOUD_PASSWORD = os.getenv('PCLOUD_PASSWORD')
PCLOUD_MUSIC_FOLDER = os.getenv('PCLOUD_MUSIC_FOLDER')

# Signup view
def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()  # This saves the user to the database
            login(request, user)  # Log the user in after successful signup
            messages.success(request, "Your account has been created and you are now logged in!")
            return redirect('song_list')  # Redirect to home page
        else:
            messages.error(request, "Signup failed. Please correct the errors below.")
    else:
        form = SignupForm()
    
    return render(request, 'signup.html', {'form': form})


# Login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Authenticate and log the user in
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have successfully logged in!")
                return redirect('song_list')  # Redirect to the home page after login
            else:
                messages.error(request, "Invalid credentials. Please try again.")
        else:
            messages.error(request, "Invalid form submission. Please correct the errors.")
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

# Index view (Home page)
def index(request):
    return render(request, 'song_list.html')  # Assuming index.html is the homepage of your app


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

# Fetch song list from pCloud
def song_list(request):
    try:
        auth_token = authenticate_pcloud()
        folder_contents = list_folder_contents(auth_token, PCLOUD_MUSIC_FOLDER)
        songs = [
            {"name": item["name"], "path": item["path"]}
            for item in folder_contents.get("metadata", {}).get("contents", [])
            if not item["isfolder"]
        ]
        return render(request, "song_list.html", {"songs": songs})
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}", status=500)

# Stream song from pCloud
def play_song(request):
    auth_token = authenticate_pcloud()
    file_path = request.GET.get('file_path')  # Song file path
    response = requests.post(
        'https://api.pcloud.com/getfilelink',
        data={'auth': auth_token, 'path': file_path}
    )
    if response.status_code == 200:
        file_link = f"https://{response.json()['hosts'][0]}{response.json()['path']}"
        return JsonResponse({"url": file_link})
    else:
        return HttpResponse("Error fetching song.", status=400)
