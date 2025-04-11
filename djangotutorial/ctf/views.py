from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.
def home(request): return render(request, 'index.html')

def challenges(request): 

    # get the data from the database

    challenges = Challenge.objects.all()

    # send the data as a context variable to the template

    return render(request, 'challenges.html', {
        'challenges': challenges,
        })

def challengesform(request):
    if request.method == 'POST': # run on submit button press
        form = ChallengeForm(request.POST)
        if form.is_valid():
            form.save() # save form data into database and in proper fields
            return render(request, 'challengesfrm.html', {'form': form, 'success': True})
    else: form = ChallengeForm() # display the form if it wasn't submitted (viewing page)
    return render(request, 'challengesform.html', {'form': form})