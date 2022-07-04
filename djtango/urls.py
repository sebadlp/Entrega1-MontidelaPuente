from django.urls import  path
from .views import una_vista, crear_persona, listado_persona, about_us
from .views import una_vista

urlpatterns = [
    path('', una_vista, name='index'),
    path('index/', una_vista, name='index'),
    path('persona/', listado_persona, name='listado_persona'),
    path('crear_persona/', crear_persona, name='crear_persona'),
    path('about/', about_us, name='about_us'),

]