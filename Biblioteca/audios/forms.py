from django import forms

class Agregar_audio(forms.Form):
    name=forms.CharField(max_length=50)
    author=forms.CharField(max_length=50)
    time=forms.FloatField()
    genero = forms.CharField(max_length=20)
    price=forms.FloatField()
    info=forms.CharField(max_length=100)