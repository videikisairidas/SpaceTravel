# stars/models.py
from django.db import models

class Stars(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=20)
    color = models.CharField(max_length=50)
    temperature = models.FloatField()
    myprompt = models.TextField(max_length=5000, null=True)

    def __str__(self):
        return self.name
