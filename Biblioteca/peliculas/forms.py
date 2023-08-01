from django import forms

class Agregar_pelicula(forms.Form):
    name=forms.CharField(max_length=50)
    year=forms.IntegerField()
    time=forms.FloatField()
    genero = forms.CharField(max_length=20)
    price=forms.FloatField()
    info=forms.CharField(max_length=100)