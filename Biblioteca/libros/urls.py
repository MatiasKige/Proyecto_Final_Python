from django.contrib import admin
from django.urls import path
from libros.views import inicio, agregar_libro, list_libros, busqueda_libro 

urlpatterns = [
    path("inicio/",inicio,name="inicio"),
    path("agregar-libro/",agregar_libro,name="agregar_libro"),
    path("list-libros/",list_libros,name="list_libros"),
    path("busqueda-libro/",busqueda_libro,name="busqueda_libro")
]