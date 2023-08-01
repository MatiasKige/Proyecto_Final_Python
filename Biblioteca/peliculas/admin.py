from django.contrib import admin
from peliculas.models import Pelicula

@admin.register(Pelicula)
class Pelicula_admin(admin.ModelAdmin):
    list_display=["name","year","time","genero","price","info"]