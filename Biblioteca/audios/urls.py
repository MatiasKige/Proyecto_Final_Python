from django.contrib import admin
from django.urls import path
from audios.views import agregar_audio, list_audios

urlpatterns = [
    path("agregar-audio/",agregar_audio,name="Agregar_un_audiolibro"),
    path("list-audios/",list_audios,name="Listado_de_audiolibros")
]