from django import forms
from libros.models import Libro

class Agregar_libro(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['name',"author","genero","year","pages","price","info", 'file']



# Al usar class Meta en un formulario basado en un modelo, 
# Django puede inferir automáticamente la estructura y las propiedades de los campos del formulario a partir del modelo,
# lo que simplifica la creación y manipulación de formularios. En este caso, al utilizar ArchivoForm, 
# Django generará los campos del formulario correspondientes a nombre y archivo basándose en el modelo Archivo.