
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$',error_messages = {'error':"Phone number must be entered in the format: '+999999999'. Up to 15 digits is allowed."})
    dob = forms.DateField()

    class Meta:
        model = User
        fields = ['first_name','last_name','username','phone_number','dob', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$',error_messages = {'error':"Phone number must be entered in the format: '+999999999'. Up to 15 digits is allowed."})
    dob = forms.DateField()
    class Meta:
        model = User
        fields = ['first_name','phone_number','dob','last_name','username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']