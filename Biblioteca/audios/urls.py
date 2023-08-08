from django.urls import path
from audios.views import Create_audio, List_audios, Detail_audio, Delete_audio

urlpatterns = [
    path("agregar-audio/",Create_audio.as_view(),name="Agregar_un_audiolibro"),
    path("list-audios/",List_audios.as_view(),name="Listado_de_audiolibros"),
    path("detail-audio/<int:pk>/",Detail_audio.as_view(),name="Detalles_del_audiolibro"),
    path("delete-audio/<int:pk>/",Delete_audio.as_view(),name="Eliminar_audio")
]