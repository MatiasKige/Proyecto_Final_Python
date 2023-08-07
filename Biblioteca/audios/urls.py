from django.contrib import admin
from django.urls import path
from audios.views import agregar_audio, list_audios, delete_audio

urlpatterns = [
    path("agregar-audio/",agregar_audio,name="Agregar_un_audiolibro"),
    path("list-audios/",list_audios,name="Listado_de_audiolibros"),
    path("delete-audio/<int:pk>",delete_audio,name="Eliminar_audio")
]