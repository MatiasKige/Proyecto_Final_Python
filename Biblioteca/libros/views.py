from libros.models import Libro
from django.views.generic import CreateView, ListView, DetailView
from django.views.generic.edit import DeleteView

############################################################################
# Agregar libros
    
class Create_libro(CreateView):
    model = Libro
    template_name = "libros/add_libro.html"
    fields = "__all__"
    success_url = "/libros/list-libros/"
    
############################################################################
# Listado de libros

class List_libros(ListView):
    model = Libro
    template_name = "libros/list_libros.html"

############################################################################
# Detalles del libro

class Detail_libro(DetailView):
    model = Libro
    template_name = "libros/detail_libro.html"

############################################################################
# Eliminar libros

class Delete_libro(DeleteView):
    model = Libro
    template_name = "libros/delete_libro.html"
    success_url = "/libros/list-libros/"
    
############################################################################