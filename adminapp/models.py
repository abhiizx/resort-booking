from django.db import models

# Create your models here.

class AddResort(models.Model):
    rno= models.IntegerField()
    des= models.TextField(max_length=100)
    ac=models.BooleanField()
    roomtype=models.CharField(max_length=100)
    bedtype=models.CharField(max_length=100)
    rate=models.DecimalField(max_digits=10,decimal_places=2)
    image=models.ImageField(upload_to='images/')
    status=models.BooleanField(default=True)
    