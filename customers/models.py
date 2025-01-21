from django.db import models

# Create your models here.
class Furniture(models.Model):
    furniture_name = models.CharField(max_length=20)
    furniture_description = models.CharField(max_length=255)
    furniture_picture = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.furniture_name
    


class Videos(models.Model):
    video_name = models.CharField(max_length=100)
    video = models.FileField(upload_to="videos/")

    def __str__(self):
        return self.video_name