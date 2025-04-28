from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Challenge)
admin.site.register(Participant)
admin.site.register(ChallengeCompletion)
admin.site.register(Operation)
admin.site.register(Notification)