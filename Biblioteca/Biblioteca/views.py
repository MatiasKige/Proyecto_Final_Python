from django.shortcuts import render
from libros.models import Libro
from audios.models import Audio
from peliculas.models import Pelicula

############################################################################
# Index

def inicio(request):
    libros = Libro.objects.all()
    peliculas = Pelicula.objects.all()
    audios = Audio.objects.all()
    archivos = (libros, peliculas, audios)
    context={
        "archivos":archivos
    }
    return render(request,"index.html",context=context)

############################################################################
# Traer todo

def archivos(request):
    libros = Libro.objects.all()
    peliculas = Pelicula.objects.all()
    audios = Audio.objects.all()
    archivos = (libros, peliculas, audios)
    context={
        "archivos":archivos
    }
    return render(request,"archivos.html",context=context)

############################################################################
# Buscador

def search(request):
    search = request.GET["search"]
    audios = Audio.objects.filter(name__icontains=search)
    libros = Libro.objects.filter(name__icontains=search)
    peliculas = Pelicula.objects.filter(name__icontains=search)
    context = {
        "audios":audios,
        "libros":libros,
        "peliculas":peliculas
        }
    return render(request, "search.html", context=context)

############################################################################
# Acerca de mi

def acerca_demi(request):
    return render(request, "acerca_demi.html",context={})

############################################################################