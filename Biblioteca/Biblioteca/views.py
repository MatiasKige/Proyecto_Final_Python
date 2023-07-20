from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

def fecha_hoy(request):
    today = datetime.today()
    return HttpResponse(f"Fecha: {today}")