from django.db import models

# Create your models here.
class Timer(models.Model):
    duration = models.IntegerField(default=25)  # Timer duration in minutes
    is_running = models.BooleanField(default=False)  # Indicates if the timer is currently running
    remaining_time = models.IntegerField(null=True)  # Remaining time in seconds
    start_time = models.DateTimeField(null=True, blank=True)  # Start time of the timer
