from django import forms
from .models import *

class ChallengeForm(forms.ModelForm):
    class Meta:
        model = Challenge
        fields = ['name', 'summary', 'flag_value', 'points']

class FlagSubmissionForm(forms.Form): flag_value = forms.CharField(max_length=100, label="Enter Flag")