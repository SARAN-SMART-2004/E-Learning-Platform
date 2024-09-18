from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.conf import settings

User = get_user_model()  # Get the user model

class TravelPlan(models.Model):
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organized_travel_plans')
    source_place = models.CharField(max_length=255)
    destination_place = models.CharField(max_length=255)
    waiting_place = models.CharField(max_length=255 ,null=True)
    date = models.DateField()
    leaving_time = models.TimeField()
    waiting_time = models.TimeField()
    message = models.TextField(blank=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    members = models.ManyToManyField(User, related_name='accepted_travel_plans')
    slug = models.CharField(max_length=20, null=True)
    

    def __str__(self):
        return f"{self.source_place} to {self.destination_place} on {self.date}"

