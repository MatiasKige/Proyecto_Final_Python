from django.db import models

class Libro(models.Model):
    name=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    genero=models.CharField(max_length=20, null=True, blank=True)
    pages=models.IntegerField()
    price=models.FloatField()
    info=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name="Libro"
        verbose_name_plural="Libros"