from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Profile


def registration(request):
    # If the user is authenticated, redirect them to the homepage
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':  # Handle POST request for form submission
        username = request.POST.get('username')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')

        # Ensure username is provided to avoid ValueError
         # Check if username already exists
        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': 'Username already exists'})

        user = User.objects.create_user(username=username, first_name=name, email=email, password=password)
        user.save()

        # Create user profile after user is saved
        profile = Profile(user=user, phone=phone)
        profile.save()

        print("User and profile saved successfully")
        return redirect('login')  # Redirect after successful registration
    
    # If it's a GET request, render the signup form
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')