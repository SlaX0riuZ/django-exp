from django.db import models
from django.contrib.auth.models import User
from time import *
from django.core.exceptions import ValidationError

# Create your models here.
class Challenge(models.Model):
    name = models.CharField(max_length=255) # consists of characters in a string
    summary = models.TextField() # similar to charfields but allow a lot more characters
    flag_value = models.CharField(max_length=255, unique=True)
    points = models.IntegerField(default=10)

    def __str__(self): return self.name

class Participant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    flags_solved = models.ManyToManyField(Challenge, blank=True, related_name='completed_by')
    total_points = models.IntegerField(default=0)

    def __str__(self): return self.user.username

    def update_points(self):
        self.total_points = sum(challenge.points for challenge in self.flags_solved.all())
        self.save()

class ChallengeCompletion(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True) # Time of Completion
    start_time = models.DateTimeField(null=True, blank=True) # Track start time
    def __str__(self): return f'{self.participant.user.username} completed {self.challenge.name}.'

class Operation(models.Model):
    running = models.BooleanField(default=False)
    timer = models.CharField(max_length=40, default='', verbose_name='Timer (March 18, 2025 15:37:25)')
    registration_window_open = models.BooleanField(default=False)

    def clean(self):
        try:
            timezone.datetime.striptime(self.timer, '%B %d, %Y %H:%M:%S')
        except ValueError:
            raise ValidationError({
                'timer': 'Timer must be in the format "March 18, 2025 15:37:25".'
            })

class Notification(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    running = models.BooleanField(default=False)
    color = models.CharField(max_length=7, default='#007bff')

    def __str__(self):
        return self.title