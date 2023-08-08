from django.shortcuts import render, redirect
from audios.models import Audio
from django.views.generic import CreateView, ListView, DetailView
from django.views.generic.edit import DeleteView

############################################################################
# Agregar audios

class Create_audio(CreateView):
    model = Audio
    template_name = "audios/add_audio.html"
    fields = "__all__"
    success_url = "/audios/list-audios/"
    
############################################################################
# Listado de audios

class List_audios(ListView):
    model = Audio
    template_name = "audios/list_audios.html"

############################################################################
# Detalles de audios

class Detail_audio(DetailView):
    model = Audio
    template_name = "audios/detail_audio.html"
    
############################################################################
# Eliminar audios

class Delete_audio(DeleteView):
    model = Audio
    template_name = "audios/delete_audio.html"
    success_url = "/audios/list-audios/"

############################################################################
