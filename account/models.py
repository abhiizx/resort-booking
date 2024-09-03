from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class CustomerDetails(models.Model):
    cid=models.IntegerField(primary_key=True)
    fname= models.CharField(max_length=100)
    lname= models.CharField(max_length=100)
    age=models.BigIntegerField()
    adhar=models.BigIntegerField()
    address=models.TextField()
    email=models.EmailField()
    phnno=models.BigIntegerField()
    user= models.ForeignKey(User,on_delete=models.CASCADE)
