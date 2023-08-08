from django.shortcuts import render, redirect
from audios.models import Audio
from audios.forms import Agregar_audio

############################################################################
# Agregar audios con formulario

def agregar_audio(request):
    if request.method == "POST":
        form = Agregar_audio(request.POST)
        if form.is_valid():
            Audio.objects.create(
                name = form.cleaned_data["name"],
                author = form.cleaned_data["author"],
                genero = form.cleaned_data["genero"],
                year = form.cleaned_data["year"],
                time = form.cleaned_data["time"],
                price = form.cleaned_data["price"],
                info = form.cleaned_data["info"]
            )
            return redirect(list_audios)
    
    elif request.method =="GET":
        form = Agregar_audio()
        context={
            "form":form
        }
        return render(request,"audios/add_audio.html",context=context)
    
############################################################################
# Listado de audios

def list_audios(request):
    audios = Audio.objects.all()
    context={
        "audios":audios
    }
    return render(request,"audios/list_audios.html",context=context)

############################################################################
# Eliminar audios

def delete_audio(request, pk):
    if request.method == "GET":
        audio = Audio.objects.get(pk=pk)
        context = {"audio":audio}
        return render(request, "audios/delete_audio.html", context=context)
    
    elif request.method == "POST":
        audio = Audio.objects.get(pk=pk)
        audio.delete()
        return redirect(list_audios)
    
############################################################################