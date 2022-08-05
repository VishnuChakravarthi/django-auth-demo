from django import forms
from django.contrib.auth.models import User
from .models import UserProfileModel


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'password', 'email')


class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfileModel
        fields = ('profile_pic', 'portfolio_link')


class UserLoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ("username", "password")
