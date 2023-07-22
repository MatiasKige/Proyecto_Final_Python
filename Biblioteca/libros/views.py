from django.shortcuts import render, redirect
from libros.models import Libro, Pelicula, Audio
from libros.forms import Agregar_libro

# Create your views here.

def agregar_libro(request):
    if request.method == "POST":
        form = Agregar_libro(request.POST)
        if form.is_valid():
            Libro.objects.create(
                name = form.cleaned_data["name"],
                author = form.cleaned_data["author"],
                pages = form.cleaned_data["pages"],
                price = form.cleaned_data["price"],
                info = form.cleaned_data["info"]
            )
            return redirect(list_libros)
    
    elif request.method =="GET":
        form = Agregar_libro()
        context={
            "form":form
        }
        return render(request,"new_libro.html",context=context)

def list_libros(request):
    libros = Libro.objects.all()
    context={
        "libros":libros
    }
    return render(request,"list_libros.html",context=context)

def busqueda_libro(request):
    search = request.GET["search"]
    libros = Libro.objects.filter(name__icontains=search)
    context = {
        "libros":libros
    }
    return render(request, "busqueda.html", context=context)

def inicio(request):
    libros = Libro.objects.all()
    audios = Audio.objects.all()
    peliculas = Pelicula.objects.all()
    archivos = (libros, audios, peliculas)
    context={
        "archivos":archivos
    }
    return render(request,"inicio.html",context=context)