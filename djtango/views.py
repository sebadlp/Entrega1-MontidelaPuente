from django.shortcuts import redirect, render
from djtango.forms import BusquedaPersona, FormEvento, FormPersona, FormProfesional, BusquedaProfesional, BusquedaEvento
from .models import Evento, Persona, Profesional
from datetime import datetime

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
        

def crear_profesional(request):  
    if request.method == 'POST':
        form = FormProfesional(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            profesional = Profesional(nombre=data.get('nombre'), apellido=data.get('apellido'), nacionalidad=data.get('nacionalidad'), profesion=data.get('profesion'))
            profesional.save()
            return redirect('listado_profesional')
        else:
            return render(request, 'crear_profesional.html', {'form': form})
    form_profesional = FormProfesional()
    return render(request, 'crear_profesional.html', {'form': form_profesional})


def listado_profesional(request):
            nombre_de_busqueda = request.GET.get('nombre')
            if nombre_de_busqueda:
                listado_profesional = Profesional.objects.filter(nombre__icontains = nombre_de_busqueda) 
            else:
                listado_profesional = Profesional.objects.all()
            form = BusquedaProfesional()    
            return render(request, 'listado_profesional.html', {'listado_profesional': listado_profesional, 'form': form})
        

def crear_evento(request):  
    if request.method == 'POST':
        form = FormEvento(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            fecha = data.get('fecha_evento')
            evento = Evento(nombre=data.get('nombre'), descripcion=data.get('descripcion'), ubicacion=data.get('ubicacion'), cupo=data.get('cupo'), fecha_evento=fecha if fecha else datetime.now())
            evento.save()
            return redirect('listado_evento')
        else:
            return render(request, 'crear_evento.html', {'form': form})
    form_evento = FormEvento()
    return render(request, 'crear_evento.html', {'form': form_evento})


def listado_evento(request):
            nombre_de_busqueda = request.GET.get('nombre')
            if nombre_de_busqueda:
                listado_evento = Evento.objects.filter(nombre__icontains = nombre_de_busqueda) 
            else:
                listado_evento = Evento.objects.all()  
            form = BusquedaEvento()    
            return render(request, 'listado_evento.html', {'listado_evento': listado_evento, 'form': form})