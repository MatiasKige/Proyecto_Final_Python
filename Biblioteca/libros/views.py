from django.shortcuts import render
from libros.models import Libro

# Create your views here.

def agregar_libro(request):
    new_libro = Libro.objects.create(
        name="Libro",
        author="Matias Omar Gigena",
        pages="1000",
        price="1500",
        info="Primer libro de prueba."
    )
    context={
        "new_libro":new_libro
    }
    return render(request,"new_libro.html",context=context)

def list_libros(request):
    libros = Libro.objects.all()
    context={
        "libros":libros
    }
    return render(request,"list_libros.html",context=context)