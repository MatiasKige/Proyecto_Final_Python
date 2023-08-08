from django.contrib import admin
from django.urls import path
from peliculas.views import Create_pelicula, List_peliculas, Detail_pelicula, Delete_pelicula

urlpatterns = [
    path("agregar-pelicula/",Create_pelicula.as_view(),name="Agregar_una_pelicula"),
    path("list-peliculas/",List_peliculas.as_view(),name="Listado_de_peliculas"),
    path("detail-pelicula/<int:pk>/",Detail_pelicula.as_view(),name="Detalles_de_pelicula"),
    path("delete-pelicula/<int:pk>/",Delete_pelicula.as_view(),name="delete_pelicula")
]