from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


# Create your models here.

class Place(models.Model):
    name = models.CharField(max_length=200)
    comment = models.CharField(max_length=200)
    lat = models.FloatField()
    lng = models.FloatField()

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='places')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('place_update_page', kwargs={'pk': self.pk})


class UserProfile(models.Model):
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='profile')
