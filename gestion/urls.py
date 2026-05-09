
from django.urls import path
from . import views


urlpatterns = [
    
    path("", views.inicio, name="inicio"),
    #Rutas para GETAll()
    path("actividades/", views.lista_actividades, name="lista_actividades"),
    path("usuarios_inscritos/", views.lista_usuarios_inscritos, name="lista_usuarios_inscritos"),
    path("monitores/", views.lista_monitores, name="lista_monitores"),
    path("salas/", views.lista_salas, name="lista_salas"),
    
    #Rutas para POST() para nuevos registros en formato JSON y para utilizar POSTMAN
    path("usuarios/registrar/", views.registrar_usuario, name="registrar_usuario"),
    path("salas/registrar/", views.registrar_sala, name="registrar_sala"),
    path("monitores/registrar/", views.registrar_monitor, name="registrar_monitor"),
    path("responsables_sala/registrar/", views.registrar_responsable_sala, name="registrar_responsable_sala"),
    path("actividades/registrar/", views.registrar_actividad, name="registrar_actividad"),
    
    
    #rutas para POST() para nuevos registros a través de formularios HTML
    path("usuarios_inscritos/nuevo/", views.crear_usuario_formulario, name="crear_usuario_formulario"),
    path("crear_sala_formulario/", views.registrar_sala_formulario, name="registrar_sala_formulario"),
    path("crear_monitor_formulario/", views.registrar_monitor_formulario, name="registrar_monitor_formulario"),
    path("crear_responsable_sala_formulario/", views.registrar_responsable_sala_formulario, name="registrar_responsable_sala_formulario"),
   path("crear_actividad_formulario/",views.registrar_actividad_formulario,name="crear_actividad_formulario"),
    #Rutas para GET() para buscar por ID
    path("usuarios/<int:usuario_id>/", views.buscar_usuario, name="buscar_usuario"),
    path("salas/<int:sala_id>/", views.buscar_sala, name="buscar_sala"),
    path("monitores/<int:monitor_id>/", views.buscar_monitor, name="buscar_monitor"),
    path("responsables_sala/<int:responsable_sala_id>/", views.buscar_responsable_sala, name="buscar_responsable_sala"),
    path("actividades/<int:actividad_id>/", views.buscar_actividad, name="buscar_actividad"),
]
