from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pothole/',null=True, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name