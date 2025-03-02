from django.db import models

class watched_series(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images')

class watched_later_series(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images')
