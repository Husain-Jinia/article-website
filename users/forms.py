
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from article.models import *
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=256, required=False)
    dob = forms.DateField()

    class Meta:
        model = User
        fields = ['first_name','last_name','username','phone_number','dob', 'email', 'password1', 'password2']

class UserRegisterProxy(forms.Form):
    CHOICES = []
    all_cat = Category.objects.all()
    for i in all_cat:
        CHOICES.append((i,i))
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=256, required=False)
    dob = forms.DateField()
    
    password1 = forms.CharField(max_length=256,required=True)
    password2 = forms.CharField(max_length=256,required=True)
    first_name = forms.CharField(max_length=256,required=True)
    last_name = forms.CharField(max_length=256,required=True)
    username = forms.CharField(max_length=256,required=True)
    category = forms.MultipleChoiceField(choices=CHOICES)

    def save(self):
        all_cat = Category.objects.all()    
        validated_data = self.cleaned_data
        user = User.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password1'])
        profile = Profile.objects.create(

            user=user,
            phone_number=validated_data['phone_number'],
            dob=validated_data['dob'],
            # category=validated_data['category']
        )
        for category in all_cat:
            if category.name in validated_data['category']:
                category.profile.add(profile)
                category.save()
        user.save()
        profile.save()
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=256, required=False)
    dob = forms.DateField()
    class Meta:
        model = User
        fields = ['first_name','phone_number','dob','last_name','username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']