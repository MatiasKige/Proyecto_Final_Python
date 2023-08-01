from django.contrib import admin
from django.urls import path, include
from Biblioteca.views import inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path("inicio/",inicio,name="inicio"),
    path("libros/",include("libros.urls")),
    path("audios/",include("audios.urls")),
    path("peliculas/",include("peliculas.urls"))
]