from django.db import models


class Persona(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad= models.IntegerField()
    fecha_creacion= models.DateField(null=True)
    
    def __str__(self):
        return f'{self.nombre}, esta en la lista de inscriptos.'
    
class Evento(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=60)
    ubicacion = models.CharField(max_length=30)
    cupo= models.IntegerField()
    fecha_evento= models.DateField(null=True)
    
    def __str__(self):
        return f'Evento: {self.nombre}.'
    
class Profesional(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    nacionalidad = models.CharField(max_length=30)
    profesion = models.CharField(max_length=30)
    
    def __str__(self):
        return f'El Dj es: {self.nombre}.'