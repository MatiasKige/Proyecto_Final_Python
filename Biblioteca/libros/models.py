from django.db import models

# Create your models here.

class Libro(models.Model):
    name=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    pages=models.IntegerField()
    price=models.FloatField()