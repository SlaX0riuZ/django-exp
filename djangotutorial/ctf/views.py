from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import *
from time import *

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
            messages.success(request, f'Form has been successfully submitted.')
            return render(request, 'challengesform.html', {'form': form, 'success': True})
        else:
            messages.error(request, f'An error has occurred while submitting your form. Please check your fields.')
    else: form = ChallengeForm() # display the form if it wasn't submitted (viewing page)
    return render(request, 'challengesform.html', {'form': form})

def participants(request):

    participants = Participant.objects.all()
    return render(request, 'participants.html', {
        'participants': participants,
    })

def submit_flag(request):
    if request.method=='POST':
        form = FlagSubmissionForm(request.POST)
        if form.is_valid():
            flag_value = form.cleaned_data['flag_value']
            try:
                challenge = Challenge.objects.get(flag_value=flag_value)
                participant = Participant.objects.get(user=request.user)
                completion, created = ChallengeCompletion.objects.get_or_create(participant=participant, challenge=challenge)
                if not completion.start_time:
                    messages.error(request, "Missing start time. Try refreshing the challenges page.")
                    # return redirect('submit_flag')
                if challenge not in participant.flags_solved.all():
                    participant.flags_solved.add(challenge) # Add challenge to flags.solved
                    participant.update_points() # Update total points
                    completion.timestamp = timezone.now() # Record completion time
                    time_taken = completion.timestamp - completion.start_time
                    completion.save()
                    messages.success(request, f'Flag submitted successfully! You earned {challenge.points} points!')
                else: messages.error(request, 'You have already submitted this flag!')
            except Challenge.DoesNotExist: messages.error(request, 'Invalid Flag, please try again.')
    else: form = FlagSubmissionForm()
    return render(request,'submit_flag.html',{'form':form})

