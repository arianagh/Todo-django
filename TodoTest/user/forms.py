from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput)


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = Profile
        fields = (
            'username',
            'first_name',
            'last_name',
            'password1',
            'password2',
            'age',
            'description'
        )
        labels = {
            "username": "یوزرنیم",
            "password1": "رمز عبور",
            "password2": "تکرار رمز عبور",
            "age": "سن",
            "first_name": "نام",
            "last_name": "نام خانوادگی",
            "description": "بایو",

        }


class UpdateUserProfile(UserChangeForm):

    password = None
    username = forms.CharField(disabled=True)

    class Meta:
        model = Profile
        fields = (
            'username',
            'first_name',
            'last_name',
            'age',
            'description',
            'image'
        )





