from django.db import models
from django.urls import reverse


# Create your models here.

class Place(models.Model):
    name = models.CharField(max_length=200)
    comment = models.CharField(max_length=200)
    lat = models.FloatField()
    lng = models.FloatField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('place_update_page', kwargs={'pk': self.pk})
