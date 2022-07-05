from django import forms

class FormPersona(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    fecha_creacion = forms.DateField(required=False)
        
class BusquedaPersona(forms.Form):
    nombre = forms.CharField(max_length=30)
    
class FormProfesional(forms.Form):   
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    nacionalidad = forms.CharField(max_length=30)
    profesion = forms.CharField(max_length=30)
    
class BusquedaProfesional(forms.Form):
    nombre = forms.CharField(max_length=30)
    
class FormEvento(forms.Form):
    nombre = forms.CharField(max_length=30)
    descripcion = forms.CharField(max_length=60)
    ubicacion = forms.CharField(max_length=30)
    cupo= forms.IntegerField()
    fecha_evento= forms.DateField(required=False)
    
class BusquedaEvento(forms.Form):
    nombre = forms.CharField(max_length=30)
    