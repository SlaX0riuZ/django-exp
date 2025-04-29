from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class ChallengeForm(forms.ModelForm):
    class Meta:
        model = Challenge
        fields = ['name', 'summary', 'flag_value', 'points']

class FlagSubmissionForm(forms.Form): flag_value = forms.CharField(max_length=100, label="Enter Flag")

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')