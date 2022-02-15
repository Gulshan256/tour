# from email.mime import image
from django.db import models

# Create your models here.

class destinations(models.Model):
    image= models.ImageField()
    name = models.CharField(max_length=150)
    desc=models.TextField()
    price = models.IntegerField()
    offer=models.BooleanField(default=False)

    def __str__(self):
        return self.name                      



