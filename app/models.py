from django.db import models

class Gallery(models.Model):
    gallery = models.CharField(max_length=40)

    class Meta:
        abstract = True

class Picture(Gallery):
    name = models.CharField(max_length=40)
    production_year = models.IntegerField()
    price = models.CharField(max_length=40)
    image = models.ImageField(upload_to='images', default='images/monalisa.jpg')

class Artist(models.Model):
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    pictures = models.ManyToManyField(Picture, related_name='artist')