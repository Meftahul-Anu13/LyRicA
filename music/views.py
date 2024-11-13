from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import SignupForm

# Signup view
def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()  # This saves the user to the database
            login(request, user)  # Log the user in after successful signup
            messages.success(request, "Your account has been created and you are now logged in!")
            return redirect('index')  # Redirect to home page
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
                return redirect('index')  # Redirect to the home page after login
            else:
                messages.error(request, "Invalid credentials. Please try again.")
        else:
            messages.error(request, "Invalid form submission. Please correct the errors.")
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

# Index view (Home page)
def index(request):
    return render(request, 'index.html')  # Assuming index.html is the homepage of your app
