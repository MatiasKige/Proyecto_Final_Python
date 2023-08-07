from django.shortcuts import render, redirect
from libros.models import Libro
from libros.forms import Agregar_libro

############################################################################
# Agregar libro con Formulario

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
        return render(request,"libros/add_libro.html",context=context)
    
############################################################################
# Listado de libros

def list_libros(request):
    libros = Libro.objects.all()
    context={
        "libros":libros
    }
    return render(request,"libros/list_libros.html",context=context)

############################################################################
# Eliminar libros

def delete_libro(request, pk):
    if request.method == "GET":
        libro = Libro.objects.get(pk=pk)
        context = {"libro":libro}
        return render(request, "libros/delete_libro.html", context=context)
    
############################################################################