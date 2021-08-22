from django import forms
from django.core import validators

def check_for_e(value): 
    if value[0].lower() != 'e': raise forms.ValidationError('NAME MUST START WITH E!')

class Users(forms.Form):
    name = forms.CharField(validators=[check_for_e])
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Email again')
    text = forms.CharField(widget=forms.Textarea)
    bot_catcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean = super().clean()
        if all_clean['email'] != all_clean['verify_email']: raise forms.ValidationError('EMAIL MUST MATCH!')