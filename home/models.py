from django.db import models
from django.utils import timezone
# Create your models here.

class Piplinedata(models.Model):
    vibrationCount = models.FloatField(default=0)
    date_created = models.DateField(default=timezone.now)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)

    def publish(self):
        self.vibrationCount = timezone.now()
        self.save()

    def __str__(self):
        return'Piplinedata : %f' % self.vibrationCount
        