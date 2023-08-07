from django import forms

class Agregar_libro(forms.Form):
    name = forms.CharField(max_length=50)
    author = forms.CharField(max_length=50)
    genero = forms.CharField(max_length=20)
    year = forms.IntegerField()
    pages = forms.IntegerField()
    price = forms.FloatField()
    info = forms.CharField(max_length=100)