from django.contrib import admin
from django.urls import path
from peliculas.views import agregar_pelicula, list_peliculas

urlpatterns = [
    path("agregar-pelicula/",agregar_pelicula,name="Agregar_una_pelicula"),
    path("list-peliculas/",list_peliculas,name="Listado_de_peliculas")
]