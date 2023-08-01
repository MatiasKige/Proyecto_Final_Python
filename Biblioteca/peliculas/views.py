from django.shortcuts import render, redirect
from peliculas.models import Pelicula
from peliculas.forms import Agregar_pelicula

############################################################################
# Agregar pelicula con formulario

def agregar_pelicula(request):
    if request.method == "POST":
        form = Agregar_pelicula(request.POST)
        if form.is_valid():
            Pelicula.objects.create(
                name = form.cleaned_data["name"],
                year = form.cleaned_data["year"],
                time = form.cleaned_data["time"],
                genero = form.cleaned_data["genero"],
                price = form.cleaned_data["price"],
                info = form.cleaned_data["info"]
            )
            return redirect(list_peliculas)
    
    elif request.method =="GET":
        form = Agregar_pelicula()
        context={
            "form":form
        }
        return render(request,"peliculas/add_pelicula.html",context=context)
    
############################################################################
# Listado de archivos

def list_peliculas(request):
    peliculas = Pelicula.objects.all()
    context={
        "peliculas":peliculas
    }
    return render(request,"peliculas/list_peliculas.html",context=context)

############################################################################