from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Usuario, Sala, Monitor, ResponsableSala, Actividad



#Put Endpoints 
@csrf_exempt
def update_usuario(request, usuario_id : int) -> JsonResponse:
    if request.method == "PUT":
        try:
            data = json.loads(request.body)
            usuario = Usuario.objects.get(id = usuario_id)
            usuario.nombre_usuario = data["nombre_usuario"]
            usuario.edad_usuario = data["edad_usuario"]
            usuario.email_usuario = data["email_usuario"]
            usuario.telefono_usuario = data["telefono_usuario"]
            usuario.save()
            
            return JsonResponse({
                "mensaje" : "Usuario actualizado correctamente"
            })
        except Usuario.DoesNotExist:
            return JsonResponse({"error": f"Usuario con ID:{usuario_id} no encontrado"}, status=404)
            
    return JsonResponse({"error": "El endpoint que quieres no es Permitido solo PUT"}, status=405)

@csrf_exempt
def update_sala(request, sala_id : int) -> JsonResponse:
    if request.method == "PUT":
        try:
            data = json.loads(request.body)
            sala = Sala.objects.get(id = sala_id)
            sala.nombre_sala = data["nombre_sala"]
            sala.capacidad_sala = data["capacidad_sala"]
            sala.ubicacion_sala = data["ubicacion_sala"]
            sala.save()

            return JsonResponse({
                "mensaje" : "Sala actualizada correctamente"
            })
        except Sala.DoesNotExist:
            return JsonResponse({"error": f"Sala con ID:{sala_id} no encontrada"}, status=404)
    return JsonResponse({"error": "El endpoint que quieres no es Permitido solo PUT"}, status=405)


@csrf_exempt
def update_monitor(request, monitor_id : int) -> JsonResponse:
    if request.method == "PUT":
        try:
            data = json.loads(request.body)
            monitor = Monitor.objects.get(id = monitor_id)
            monitor.nombre = data["nombre"]
            monitor.especializacion = data["especializacion"]
            monitor.save()

            return JsonResponse({
                "mensaje" : "Monitor actualizado correctamente"
            })
        except Monitor.DoesNotExist:
            return JsonResponse({"error": f"Monitor con ID:{monitor_id} no encontrado"}, status=404)
    return JsonResponse({"error": "El endpoint que quieres no es Permitido solo PUT"}, status=405)


@csrf_exempt
def update_responsable_sala(request, responsable_sala_id : int) -> JsonResponse:
    if request.method == "PUT":
        try:
            data = json.loads(request.body)
            responsable_sala = ResponsableSala.objects.get(id = responsable_sala_id)
            responsable_sala.nombre_responsable = data["nombre_responsable"]
            responsable_sala.telefono_responsable = data["telefono_responsable"]
            responsable_sala.email_responsable = data["email_responsable"]
            responsable_sala.save()

            return JsonResponse({
                "mensaje" : "Responsable de sala actualizado correctamente"
            })
        except ResponsableSala.DoesNotExist:
            return JsonResponse({"error": f"Responsable de sala con ID:{responsable_sala_id} no encontrado"}, status=404)
    return JsonResponse({"error": "El endpoint que quieres no es Permitido solo PUT"}, status=405)

@csrf_exempt
def update_actividad(request, actividad_id : int) -> JsonResponse:
    if request.method == "PUT":
        try:
            data = json.loads(request.body)
            actividad = Actividad.objects.get(id = actividad_id)
            actividad.nombre_actividad = data["nombre_actividad"]
            actividad.tipo_actividad = data["tipo_actividad"]
            actividad.horario_actividad = data["horario_actividad"]
            actividad.descripcion_actividad = data["descripcion_actividad"]
            actividad.duracion_actividad = data["duracion_actividad"]
            actividad.plazas_disponibles = data["plazas_disponibles"]
            actividad.save()

            return JsonResponse({
                "mensaje" : "Actividad actualizada correctamente"
            })
        except Actividad.DoesNotExist:
            return JsonResponse({"error": f"Actividad con ID:{actividad_id} no encontrada"}, status=404)
    
    return JsonResponse({"error": "El endpoint que quieres no es Permitido solo PUT"}, status=405)     
