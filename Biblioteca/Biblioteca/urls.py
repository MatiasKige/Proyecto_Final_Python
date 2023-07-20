from django.contrib import admin
from django.urls import path, include
from Biblioteca.views import fecha_hoy

urlpatterns = [
    path('admin/', admin.site.urls),
    path("fecha-hoy/",fecha_hoy,name="fecha_hoy"),
    path("libros/",include("libros.urls"))
]
