from django.db import models

# Create your models here.
class FormMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    send_time = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    