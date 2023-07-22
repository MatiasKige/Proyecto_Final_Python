from django.http import HttpResponse
from datetime import datetime

def fecha_hoy(request):
    today = datetime.today()
    return HttpResponse(f"Fecha: {today}")