from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

def fecha_hoy(request):
    today = datetime.today()
    return HttpResponse(f"Fecha: {today}")

def template_list(request):
    list = ["1,2,3,4,5"]
    context={
        "list":list
    }
    return render(request,"template_list.html",context=context)