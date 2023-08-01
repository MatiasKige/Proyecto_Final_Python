from django.contrib import admin
from libros.models import Libro

@admin.register(Libro)
class Libro_admin(admin.ModelAdmin):
    list_display=["name","author","genero","pages","price","info"]