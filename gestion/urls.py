
from django.urls import path
from . import views
from . import views_get
from . import views_post
from . import views_put
from . import views_delete


urlpatterns = [
    
    path("", views.inicio, name="inicio"),
    #Rutas para GETAll() y filtros
    path("actividades/", views_get.filtrar_actividades, name="filtrar_actividades"),
    path("usuarios/", views_get.filtrar_usuarios, name="filtrar_usuarios"),
    path("usuarios_inscritos/", views_get.lista_usuarios_inscritos, name="lista_usuarios_inscritos"),
    path("monitores/", views_get.lista_monitores, name="lista_monitores"),
    path("salas/", views_get.lista_salas, name="lista_salas"),
    
    #Rutas para POST() para nuevos registros en formato JSON y para utilizar POSTMAN
    path("usuarios/registrar/", views_post.registrar_usuario, name="registrar_usuario"),
    path("salas/registrar/", views_post.registrar_sala, name="registrar_sala"),
    path("monitores/registrar/", views_post.registrar_monitor, name="registrar_monitor"),
    path("responsables_sala/registrar/", views_post.registrar_responsable_sala, name="registrar_responsable_sala"),
    path("actividades/registrar/", views_post.registrar_actividad, name="registrar_actividad"),
    
    
    #rutas para POST() para nuevos registros a través de formularios HTML
    path("usuarios_inscritos/nuevo/", views_post.crear_usuario_formulario, name="crear_usuario_formulario"),
    path("crear_sala_formulario/", views_post.registrar_sala_formulario, name="registrar_sala_formulario"),
    path("crear_monitor_formulario/", views_post.registrar_monitor_formulario, name="registrar_monitor_formulario"),
    path("crear_responsable_sala_formulario/", views_post.registrar_responsable_sala_formulario, name="registrar_responsable_sala_formulario"),
    path("crear_actividad_formulario/",views_post.registrar_actividad_formulario,name="crear_actividad_formulario"),
    
    #Rutas para GET() para buscar por ID
    path("usuarios/<int:usuario_id>/", views_get.buscar_usuario, name="buscar_usuario"),
    path("salas/<int:sala_id>/", views_get.buscar_sala, name="buscar_sala"),
    path("monitores/<int:monitor_id>/", views_get.buscar_monitor, name="buscar_monitor"),
    path("responsables_sala/<int:responsable_sala_id>/", views_get.buscar_responsable_sala, name="buscar_responsable_sala"),
    path("actividades/<int:actividad_id>/", views_get.buscar_actividad, name="buscar_actividad"),
    
    #Rutas para PUT() para actualizar por ID
    path("usuarios/<int:usuario_id>/editar/", views_put.update_usuario, name="update_usuario"),
    path("salas/<int:sala_id>/editar/", views_put.update_sala, name="update_sala"),
    path("monitores/<int:monitor_id>/editar", views_put.update_monitor, name="update_monitor"),
    path("responsables_sala/<int:responsable_sala_id>/editar", views_put.update_responsable_sala, name="update_responsable_sala"),
    path("actividades/<int:actividad_id>/editar", views_put.update_actividad, name="update_actividad"),
    
    #Rutas para DELETE() para eliminar por ID
    path("usuarios/<int:usuario_id>/eliminar/", views_delete.delete_usuario, name="eliminar_usuario"),
    path("salas/<int:sala_id>/eliminar/", views_delete.delete_sala, name="eliminar_sala"),
    path("monitores/<int:monitor_id>/eliminar/", views_delete.delete_monitor, name="eliminar_monitor"),
    path("responsables_sala/<int:responsable_sala_id>/eliminar/", views_delete.delete_responsable_sala, name="eliminar_responsable_sala"),
    path("actividades/<int:actividad_id>/eliminar/", views_delete.delete_actividad, name="eliminar_actividad"),
 
 
    #Rutas para Inscripciones
    path("actividades/<int:actividad_id>/inscripciones/", views_get.listar_inscripciones_actividad, name="listar_inscripciones_actividad"),
    path("actividades/<int:actividad_id>/inscribir/", views_post.inscribir_usuario_actividad_formulario, name="inscribir_usuario_actividad_formulario"),
    path("actividades/<int:actividad_id>/inscripciones/<int:usuario_id>/eliminar/", views_post.eliminar_inscripcion_actividad, name="eliminar_inscripcion_actividad"),
]
