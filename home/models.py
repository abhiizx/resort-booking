from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    img = models.ImageField(upload_to='images/')  # Adjust as necessary

    def __str__(self):
        return self.name

# Create your models here.
