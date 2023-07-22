from django.db import models

# Create your models here.

class Libro(models.Model):
    name=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    pages=models.IntegerField()
    price=models.FloatField()
    info=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name="Libro"
        verbose_name_plural="Libros"

class Pelicula(models.Model):
    name=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    pages=models.IntegerField()
    price=models.FloatField()
    info=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name="Pelicula"
        verbose_name_plural="Peliculas"

class Audio(models.Model):
    name=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    pages=models.IntegerField()
    price=models.FloatField()
    info=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name="Audio"
        verbose_name_plural="Audios"