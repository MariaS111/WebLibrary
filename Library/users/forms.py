from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class UserRegisterForm(UserCreationForm):
    username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    avatar = forms.ImageField(required=False)
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'avatar', 'password1', 'password2']