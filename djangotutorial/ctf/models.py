from django.db import models
from django.contrib.auth.models import User

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