from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from NewApp.forms import FormUser, FormUserProfile

from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'NewApp/index.html')

def register(request):
    register = False

    if request.method == 'POST':
        user_form = FormUser(data=request.POST)
        profile_form = FormUserProfile(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile =profile_form.save(commit=False)
            profile.user = user

            if 'image_ProfilePicture' in request.FILES:
                profile.image_ProfilePicture = request.FILES['image_ProfilePicture']

            profile.save()
            register = True

        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = FormUser()
        profile_form = FormUserProfile()
        
    return render(request, 'NewApp/register.html', context={'register':register, 'user_form':user_form, 'profile_form':profile_form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            else: return HttpResponse(f'{username.title()} is not active!')

        else: return HttpResponse(f'{username.title()}, invalid password')
        
    else: return render(request, 'NewApp/login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))