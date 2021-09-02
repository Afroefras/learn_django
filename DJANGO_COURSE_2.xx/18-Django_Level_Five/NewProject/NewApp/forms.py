from django import forms
from django.contrib.auth.models import User
from django.db.models import fields
from NewApp.models import ModelUserProfile

class FormUser(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class FormUserProfile(forms.ModelForm):
    class Meta:
        model = ModelUserProfile
        fields = ('url_LinkedIn', 'image_ProfilePicture')