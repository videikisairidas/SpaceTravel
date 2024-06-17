# kometa/models.py

from django.db import models

class Comets(models.Model):
    name = models.CharField(max_length=100)
    size = models.FloatField()
    color = models.CharField(max_length=50)
    tail = models.BooleanField()
    myprompt = models.TextField(max_length=5000, null=True)

    def __str__(self):
        return self.name
