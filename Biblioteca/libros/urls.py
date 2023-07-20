from django.contrib import admin
from django.urls import path
from libros.views import agregar_libro, list_libros

urlpatterns = [
    path('admin/', admin.site.urls),
    path("agregar-libro/",agregar_libro,name="agregar_libro"),
    path("list-libros/",list_libros,name="list_libros")
]