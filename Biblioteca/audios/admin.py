from django.contrib import admin
from audios.models import Audio

@admin.register(Audio)
class Audio_admin(admin.ModelAdmin):
    list_display = ["name","author","genero","year","time","price","info"]