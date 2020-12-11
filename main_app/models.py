from django.db import models
from django.urls import reverse

# Create your models here.
class Pedal(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    def __str__(self):
        return self.name

    # add absolute url instead of creating a success url in PedalClass view 
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pedal_id': self.id})