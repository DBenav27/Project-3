from django.db import models
from django.contrib.auth.models import User



class Treasure(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    age = models.DecimalField(max_digits=10, decimal_places=0)
    gender = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    about = models.CharField(max_length=100, default='')
    dog = models.CharField(max_length=100, default='')
    breed = models.CharField(max_length=100, default='')
    likes = models.IntegerField(default=0)
    image = models.ImageField(upload_to='treasure_images',
                               default='')

    def __str__(self):
        return self.name
