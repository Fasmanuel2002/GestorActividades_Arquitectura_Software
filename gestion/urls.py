
from django.urls import path

from .views import (
    lista_actividades,
    list_usuarios_inscritos,
    lista_monitores,
    lista_salas,
    registrar_usuario,
    registrar_sala,
    registrar_monitor,
    registrar_responsable_sala,
    registrar_actividad,
    buscar_usuario,
    buscar_sala,
    buscar_monitor,
    buscar_responsable_sala,
    buscar_actividad,
)


urlpatterns = [
    path("actividades/", lista_actividades, name="lista_actividades"),
    path("usuarios_inscritos/", list_usuarios_inscritos, name="list_usuarios_inscritos"),
    path("monitores/", lista_monitores, name="lista_monitores"),
    path("salas/", lista_salas, name="lista_salas"),
    path("usuarios/registrar/", registrar_usuario, name="registrar_usuario"),
    path("salas/registrar/", registrar_sala, name="registrar_sala"),
    path("monitores/registrar/", registrar_monitor, name="registrar_monitor"),
    path("responsables_sala/registrar/", registrar_responsable_sala, name="registrar_responsable_sala"),
    path("actividades/registrar/", registrar_actividad, name="registrar_actividad"),
    path("usuarios/<int:usuario_id>/", buscar_usuario, name="buscar_usuario"),
    path("salas/<int:sala_id>/", buscar_sala, name="buscar_sala"),
    path("monitores/<int:monitor_id>/", buscar_monitor, name="buscar_monitor"),
    path("responsables_sala/<int:responsable_sala_id>/", buscar_responsable_sala, name="buscar_responsable_sala"),
    path("actividades/<int:actividad_id>/", buscar_actividad, name="buscar_actividad"),
]
