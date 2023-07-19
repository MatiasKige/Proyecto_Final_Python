from django.contrib import admin
from django.urls import path
from Biblioteca.views import fecha_hoy, template_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path("fecha-hoy/",fecha_hoy,name="fecha_hoy"),
    path("template-list/",template_list,name="template_list")
]
