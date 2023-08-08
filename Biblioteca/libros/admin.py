from django.contrib import admin
from libros.models import Libro

@admin.register(Libro)
class Libro_admin(admin.ModelAdmin):
    list_display=["name","author","genero","year","pages","price","info"]