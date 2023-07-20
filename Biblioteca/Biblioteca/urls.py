from django.contrib import admin
from django.urls import path
from Biblioteca.views import fecha_hoy
from libros.views import agregar_libro, list_libros

urlpatterns = [
    path('admin/', admin.site.urls),
    path("fecha-hoy/",fecha_hoy,name="fecha_hoy"),
    path("agregar-libro/",agregar_libro,name="agregar_libro"),
    path("list-libros/",list_libros,name="list_libros")
]
