from django.contrib import admin
from django.urls import path, include
from Biblioteca.views import inicio, archivos, search, acerca_demi

urlpatterns = [
    path('admin/', admin.site.urls),
    path("archivos/",archivos,name="Todo_el_contenido"),
    path("",inicio,name="index"),
    path("libros/",include("libros.urls")),
    path("audios/",include("audios.urls")),
    path("peliculas/",include("peliculas.urls")),
    path("search/",search,name="search"),
    path("acerca-demi/",acerca_demi,name="Acerca_de_mi")
]