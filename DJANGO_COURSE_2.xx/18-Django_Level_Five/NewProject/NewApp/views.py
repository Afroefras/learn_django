from django.contrib.auth.models import User
from django.shortcuts import render
from NewApp.forms import FormUser, FormUserProfile

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
