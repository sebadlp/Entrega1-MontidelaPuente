from django.http import HttpResponse
from django.shortcuts import redirect, render

from djtango.forms import BusquedaPersona, FormPersona
from .models import Persona
from django.template import loader
from datetime import datetime

# Create your views here.

def una_vista(request):
    return render(request, 'index.html')

def about_us(request):
    return render(request, 'about.html')

def crear_persona(request):  
   
    if request.method == 'POST':
        form = FormPersona(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            
            fecha = data.get('fecha_creacion')
            
            persona = Persona(nombre=data.get('nombre'), apellido=data.get('apellido'), edad=data.get('edad'), fecha_creacion=fecha if fecha else datetime.now())
            persona.save()

            return redirect('listado_persona')
        
        else:
            return render(request, 'crear_persona.html', {'form': form})
        
    form_persona = FormPersona()
    
    
    return render(request, 'crear_persona.html', {'form': form_persona})


def listado_persona(request):
    
            nombre_de_busqueda = request.GET.get('nombre')
            
            if nombre_de_busqueda:
                listado_persona = Persona.objects.filter(nombre__icontains = nombre_de_busqueda) 
            else:
                listado_persona = Persona.objects.all()
                
            form = BusquedaPersona()    
            return render(request, 'listado_persona.html', {'listado_persona': listado_persona, 'form': form})