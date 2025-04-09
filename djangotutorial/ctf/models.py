from django.db import models

# Create your models here.
class Challenge(models.Model):
    name = models.CharField(max_length=255) # consists of characters in a string
    summary = models.TextField() # similar to charfields but allow a lot more characters
    flag_value = models.CharField(max_length=255, unique=True)
    points = models.IntegerField(default=10)

    def __str__(self):
        return self.name