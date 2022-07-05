from django.urls import  path
from .views import una_vista, crear_persona, listado_persona, about_us, crear_profesional, crear_evento, listado_profesional, listado_evento
from .views import una_vista

urlpatterns = [
    path('', una_vista, name='index'),
    path('index/', una_vista, name='index'),
    path('persona/', listado_persona, name='listado_persona'),
    path('crear_persona/', crear_persona, name='crear_persona'),
    path('about/', about_us, name='about_us'),
    path('crear_profesional/', crear_profesional, name='crear_profesional'),
    path('crear_evento/', crear_evento, name='crear_evento'),
    path('profesional/', listado_profesional, name='listado_profesional'),
    path('evento/', listado_evento, name='listado_evento'),

]