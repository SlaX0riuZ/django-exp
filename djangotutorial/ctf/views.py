from django.shortcuts import render
from .models import *

# Create your views here.
def home(request): return render(request, 'index.html')

def challenges(request): 

    # get the data from the database

    challenges = Challenge.objects.all()

    # send the data as a context variable to the template

    return render(request, 'challenges.html', {
        'challenges': challenges,
        })