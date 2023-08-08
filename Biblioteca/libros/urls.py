from django.urls import path
from libros.views import Create_libro, List_libros, Detail_libro, Delete_libro

urlpatterns = [
    path("agregar-libro/",Create_libro.as_view(),name="Agregar_un_libro"),
    path("list-libros/",List_libros.as_view(),name="Listado_de_libros"),
    path("detail-libro/<int:pk>/",Detail_libro.as_view(),name="Detalles_del_libro"),
    path("delete-libro/<int:pk>/",Delete_libro.as_view(),name="Eliminar_libro")
]