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