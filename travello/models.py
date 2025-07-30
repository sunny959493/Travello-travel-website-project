from django.db import models

class destination(models.Model):
    name = models.TextField(max_length=100)
    price = models.IntegerField()
    desc = models.TextField(max_length=200)
    img = models.ImageField(upload_to='pics')
    offer = models.BooleanField(default=False)

class t_destination(models.Model):
    name = models.TextField(max_length=100)
    price = models.IntegerField()
    desc = models.TextField(max_length=200)
    img = models.ImageField(upload_to='pics')