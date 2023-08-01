from django.db import models

class Pelicula(models.Model):
    name=models.CharField(max_length=50)
    year=models.IntegerField()
    time=models.FloatField()
    genero=models.CharField(max_length=20, null=True, blank=True)
    price=models.FloatField()
    info=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name="Pelicula"
        verbose_name_plural="Peliculas"