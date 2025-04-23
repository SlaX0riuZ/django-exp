from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import *
from .forms import *
from django.utils import timezone

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

def challenges(request):
    challenges = Challenge.objects.all()
    participant = None
    solved_challenge_ids = []
    if request.user.is_authenticated:
        participant = Participant.objects.get(user=request.user)
        solved_challenge_ids = participant.flags_solved.values_list('id', flat=True) # Gets IDs of solved challenges
        print(f'Participant: {participant}, Type: {type(participant)}') # Debugging
        print(f'Solved Challenges: {solved_challenge_ids}') # Debugging
    return render(request, 'challenges.html', {
        'challenges': challenges,
        'participant': participant,
        'solved_challenge_ids': solved_challenge_ids,
        # No 'notify' or 'operations' here.
    })

def challenge_detail(request, challenge_id):
    challenge = get_object_or_404(Challenge, id=challenge_id)
    return render(request, 'challenge_detail.html', {'challenge':challenge}) # no notify or operations

def start_challenge(request, challenge_id):
    challenge = get_object_or_404(Challenge, id=challenge_id)
    participant, created = Participant.objects.get_or_create(user=request.user)
    completion, created = ChallengeCompletion.objects.get_or_create(
        participant = participant, challenge = challenge
    )

    if not completion.start_time:
        completion.start_time = timezone.now()
        completion.save()
        return JsonResponse({'status': 'success', 'message': 'Challenge Started!'})
    return JsonResponse({'status': 'exists', 'message': 'Challenge Already Started!'})