from django import forms
from app_model_forms.models import Users

class NewUserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = '__all__'