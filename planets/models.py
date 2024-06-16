from django.db import models

# Create your models here.
class Planets(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)

    def __str__(self):
        return self.name


class Objects(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    planetID = models.ForeignKey(Planets, on_delete=models.CASCADE)

    def __str__(self):
        return self.name