
from django.urls import path

from .views import (
    lista_actividades,
    list_usuarios_inscritos,
    lista_monitores,
    lista_salas,
)


urlpatterns = [
    path("actividades/", lista_actividades, name="lista_actividades"),
    path("usuarios_inscritos/", list_usuarios_inscritos, name="list_usuarios_inscritos"),
    path("monitores/", lista_monitores, name="lista_monitores"),
    path("salas/", lista_salas, name="lista_salas"),
]
