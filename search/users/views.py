from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm 
from .models import Profile
# create flash messages in sessions which can be rendered (check main.html)
from django.contrib import messages

def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}  
    return render(request, 'users/profiles.html', context)

def login_user(request):

    page = 'login'
    context = {'page':page}

    # prevents from typing the login page -- when already logged in
    # only POST method can change the login now
    if request.user.is_authenticated:
        return redirect('profiles')


    if request.method  == 'POST':
        # gets a dict with csrftoken, username, and passwordS
        username = request.POST['username']
        password = request.POST['password']
        
        # validate certain things
        try:
            # checks with Django User models and not our profiles
            user = User.objects.get(username = username)
        except:
            messages.error(request, 'Username does not exist')

        # query django DB to see if username and password match
        user = authenticate(request, username = username, password = password)

        if user is not None:
            # logs in the user w their respective credentials
            # starts a new session id in Django auth
            login(request, user)
            messages.success(request, user.username + ' account was logged in!')
            return redirect('profiles')
        else:
            messages.error(request, 'Username or password is incorrect')
    return render(request, "users/login_register.html", context)


def logout_user(request):
    # just deletes the current session 
    logout(request)
    messages.info(request, 'User was logged out')
    return redirect('login')

def register_user(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # commit False holds the user temporarily to modify it before processing it
            # such as making it not case sensitive to reduce errors
            user = form.save(commit = False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, user.username + ' account was created!')
            login(request, user)
            messages.success(request, user.username + ' account was logged in!')
            return redirect('profiles')
        else:
            messages.error(request, ' An error has occurred during registration')

    context = {'page':page, 'form': form}
    return render(request, 'users/login_register.html', context)

def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    # if skill does not have any description, it will not be displayed
    topSkills = profile.skill_set.exclude(description__exact='')
    otherSkills = profile.skill_set.filter(description='')
    context = {'profile': profile, 'padding': '15px', 
               'topSkills': topSkills, 'otherSkills': otherSkills}
    return render(request, 'users/user-profile.html', context)