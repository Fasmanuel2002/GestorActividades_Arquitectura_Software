from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .models import Usuario, Sala, Monitor, ResponsableSala, Actividad

"""
GET ALL LIST
"""
def lista_actividades(request):
    actividades = Actividad.objects.all()
    return render(request, "gestion/lista_actividades.html", {"actividades": actividades})

def list_usuarios_inscritos(request):
    usuarios_inscritos = Usuario.objects.all()
    return render(request, "gestion/lista_usuarios_inscritos.html", {"usuarios_inscritos": usuarios_inscritos})

def lista_monitores(request):
    monitores = Monitor.objects.all()
    return render(request, "gestion/lista_monitores.html", {"monitores": monitores})

def lista_salas(request):
    salas = Sala.objects.all()
    return render(request, "gestion/lista_salas.html", {"salas": salas})


"""
POST ENDPOINTS
"""
@csrf_exempt
def registrar_usuario(request) -> JsonResponse:
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            usuario = Usuario.objects.create(
                nombre_usuario=data['nombre_usuario'],
                edad_usuario=data['edad_usuario'],
                email_usuario=data['email_usuario'],
                telefono_usuario=data['telefono_usuario']
            )
            return JsonResponse({
                "mensaje": "Usuario registrado con éxito",
                "usuario_id": usuario.id
            })
        except KeyError:
            return JsonResponse({"error": "Datos incompletos"}, status=400)
    return JsonResponse({"error": "Método no permitido"}, status=405)


@csrf_exempt
def registrar_sala(request) -> JsonResponse:
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            sala = Sala.objects.create(
                nombre_sala=data['nombre_sala'],
                capacidad_sala=data['capacidad_sala'],
                ubicacion_sala=data['ubicacion_sala']
            )
            return JsonResponse({
                "mensaje": "Sala registrada con éxito",
                "sala_id": sala.id
            })
        except KeyError:
            return JsonResponse({"error": "Datos incompletos"}, status=400)
    return JsonResponse({"error": "Método no permitido"}, status=405)


@csrf_exempt
def registrar_monitor(request) -> JsonResponse:
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            monitor = Monitor.objects.create(
                nombre=data['nombre'],
                especializacion=data['especializacion']
            )
            return JsonResponse({
                "mensaje": "Monitor registrado con éxito",
                "monitor_id": monitor.id
            })
        except KeyError:
            return JsonResponse({"error": "Datos incompletos"}, status=400)
    return JsonResponse({"error": "Método no permitido"}, status=405)


@csrf_exempt
def registrar_responsable_sala(request) -> JsonResponse:
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            sala = Sala.objects.get(id=data['sala_id'])
            responsable_sala = ResponsableSala.objects.create(
                nombre_responsable=data['nombre_responsable'],
                telefono_responsable=data['telefono_responsable'],
                email_responsable=data['email_responsable'],
                sala=sala
            )
            return JsonResponse({
                "mensaje": "Responsable de sala registrado con éxito",
                "responsable_sala_id": responsable_sala.id
            })
        except Sala.DoesNotExist:
            return JsonResponse({"error": "Sala no encontrada"}, status=404)
        except KeyError:
            return JsonResponse({"error": "Datos incompletos"}, status=400)
    return JsonResponse({"error": "Método no permitido"}, status=405)


@csrf_exempt
def registrar_actividad(request) -> JsonResponse:
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            monitor = Monitor.objects.get(id=data['monitor_actividad_id'])
            sala_principal = Sala.objects.get(id=data['sala_principal_id'])
            actividad = Actividad.objects.create(
                nombre_actividad=data['nombre_actividad'],
                tipo_actividad=data['tipo_actividad'],
                horario_actividad=data['horario_actividad'],
                descripcion_actividad=data['descripcion_actividad'],
                duracion_actividad=data['duracion_actividad'],
                plazas_disponibles=data['plazas_disponibles'],
                monitor_actividad=monitor,
                sala_principal=sala_principal
            )
            return JsonResponse({
                "mensaje": "Actividad registrada con éxito",
                "actividad_id": actividad.id
            })
        except Monitor.DoesNotExist:
            return JsonResponse({"error": "Monitor no encontrado"}, status=404)
        except Sala.DoesNotExist:
            return JsonResponse({"error": "Sala principal no encontrada"}, status=404)
        except KeyError:
            return JsonResponse({"error": "Datos incompletos"}, status=400)
    return JsonResponse({"error": "Método no permitido"}, status=405)
