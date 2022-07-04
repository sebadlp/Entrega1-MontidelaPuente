from django import forms

class FormPersona(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    fecha_creacion = forms.DateField(required=False)
    
    
class BusquedaPersona(forms.Form):
    nombre = forms.CharField(max_length=30)