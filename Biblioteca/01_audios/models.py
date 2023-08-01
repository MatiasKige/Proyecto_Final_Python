from django.db import models

class Audio(models.Model):
    name=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    time=models.IntegerField()
    genero=models.CharField(max_length=20, null=True, blank=True)
    price=models.FloatField()
    info=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name="Audio"
        verbose_name_plural="Audios"