from django.contrib import admin
from django.urls import path
from libros.views import agregar_libro ,list_libros

urlpatterns = [
    path("agregar-libro/",agregar_libro,name="Agregar_un_libro"),
    path("list-libros/",list_libros,name="Listado_de_libros")
]