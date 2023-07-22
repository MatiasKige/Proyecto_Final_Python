from django.contrib import admin
from libros.models import Libro

# Register your models here.

@admin.register(Libro)
class Libro_admin(admin.ModelAdmin):
    list_display=["name","author","pages","price","info"]