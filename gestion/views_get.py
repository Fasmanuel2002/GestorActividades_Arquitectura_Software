from django.http import JsonResponse
from django.shortcuts import render
from .models import Usuario, Sala, Monitor, ResponsableSala, Actividad

"""
GET ALL LIST
"""
def lista_actividades(request):
    actividades = Actividad.objects.all()
    return render(request, "gestion/GET_ALL/lista_actividades.html", {"actividades": actividades})

def lista_usuarios_inscritos(request):
    usuarios_inscritos = Usuario.objects.all()
    return render(request, "gestion/GET_ALL/lista_usuarios_inscritos.html", {"usuarios_inscritos": usuarios_inscritos})

def lista_monitores(request):
    monitores = Monitor.objects.all()
    return render(request, "gestion/GET_ALL/lista_monitores.html", {"monitores": monitores})

def lista_salas(request):
    salas = Sala.objects.all()
    return render(request, "gestion/GET_ALL/lista_salas.html", {"salas": salas})

def lista_responsables_sala(request):
    responsables_sala = ResponsableSala.objects.all()
    return render(request, "gestion/GET_ALL/lista_responsables_sala.html", {"responsables_sala": responsables_sala})




"""
GET By ID ENDPOINTS
"""
def buscar_usuario(request, usuario_id):
    try:
        usuario = Usuario.objects.values(
            'id',
            'nombre_usuario',
            'edad_usuario',
            'email_usuario',
            'telefono_usuario'
        ).get(id=usuario_id)
        return JsonResponse(usuario)
    except Usuario.DoesNotExist:
        return JsonResponse({"error": "Usuario no encontrado"}, status=404)


def buscar_sala(request, sala_id : int) -> JsonResponse:
    try:
        sala = Sala.objects.values(
            'id',
            'nombre_sala',
            'capacidad_sala',
            'ubicacion_sala'
        ).get(id=sala_id)
        return JsonResponse(sala)
    except Sala.DoesNotExist:
        return JsonResponse({"error": "Sala no encontrada"}, status=404)


def buscar_monitor(request, monitor_id : int) -> JsonResponse:
    try:
        monitor = Monitor.objects.values(
            'id',
            'nombre',
            'especializacion'
        ).get(id=monitor_id)
        return JsonResponse(monitor)
    except Monitor.DoesNotExist:
        return JsonResponse({"error": "Monitor no encontrado"}, status=404)


def buscar_responsable_sala(request, responsable_sala_id : int) -> JsonResponse:
    try:
        responsable_sala = ResponsableSala.objects.values(
            'id',
            'nombre_responsable',
            'telefono_responsable',
            'email_responsable',
            'sala_id'
        ).get(id=responsable_sala_id)
        return JsonResponse(responsable_sala)
    except ResponsableSala.DoesNotExist:
        return JsonResponse({"error": "Responsable de sala no encontrado"}, status=404)


def buscar_actividad(request, actividad_id : int) -> JsonResponse:
    try:
        actividad = Actividad.objects.values(
            'id',
            'nombre_actividad',
            'tipo_actividad',
            'horario_actividad',
            'descripcion_actividad',
            'duracion_actividad',
            'plazas_disponibles',
            'monitor_actividad_id',
            'sala_principal_id'
        ).get(id=actividad_id)
        return JsonResponse(actividad)
    except Actividad.DoesNotExist:
        return JsonResponse({"error": "Actividad no encontrada"}, status=404)

