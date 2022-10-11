from email.policy import default
from turtle import title
from django.db import models

class Resttaurnt(models.Model):

    name = models.CharField(max_length=30)
    description = models.TextField(default="") 
    opening_time = models.TimeField()
    closing_time = models.TextField()
    created_at = models.DateField(auto_now_add=True)

