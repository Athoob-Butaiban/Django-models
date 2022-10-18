from email.policy import default
from turtle import title
from django.db import models

class Restaurant(models.Model):

    name = models.CharField(max_length=30)
    description = models.TextField(default="") 
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    created_at = models.DateField(auto_now_add=True)

