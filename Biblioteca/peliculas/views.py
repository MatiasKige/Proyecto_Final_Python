from django.shortcuts import render, redirect
from peliculas.models import Pelicula
from django.views.generic import CreateView, ListView, DetailView
from django.views.generic.edit import DeleteView

############################################################################
# Agregar peliculas
    
class Create_pelicula(CreateView):
    model = Pelicula
    template_name = "peliculas/add_pelicula.html"
    fields = "__all__"
    success_url = "/peliculas/list-peliculas/"
    
############################################################################
# Listado de archivos

class List_peliculas(ListView):
    model = Pelicula
    template_name = "peliculas/list_peliculas.html"

############################################################################
# Eliminar peliculas

class Detail_pelicula(DetailView):
    model = Pelicula
    template_name = "peliculas/detail_pelicula.html"

############################################################################
# Eliminar peliculas

class Delete_pelicula(DeleteView):
    model = Pelicula
    template_name = "peliculas/delete_pelicula.html"
    success_url = "/peliculas/list-peliculas/"
    
############################################################################