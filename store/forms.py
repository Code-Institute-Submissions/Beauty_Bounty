from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(
        max_length=300, help_text="eg. typeemail@gmail.com")

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'username','password1', 'password2', 'email')
