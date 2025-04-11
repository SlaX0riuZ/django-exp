from django import forms
from .models import *

class ChallengeForm(forms.ModelForm):
    class Meta:
        model = Challenge
        fields = ['name', 'summary', 'flag_value', 'points']