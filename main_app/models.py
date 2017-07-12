from django.db import models
from django.contrib.auth.models import User



class Treasure(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    age = models.DecimalField(max_digits=10, decimal_places=2)
    gender = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    likes = models.IntegerField(default=0)
    image = models.ImageField(upload_to='treasure_images',
                               default='media/default.png')


    def __str__(self):
        return self.name
