from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Usuario, Sala, Monitor, ResponsableSala, Actividad


@csrf_exempt
def delete_usuario(request, usuario_id : int) -> JsonResponse:
    if request.method == "DELETE":
        try:
            usuario = Usuario.objects.get(id = usuario_id)
            usuario.delete()
            return JsonResponse({
                "mensaje" : f"El usuario con id {usuario_id} ha sido eliminado correctamente "})
            
        except Usuario.DoesNotExist:
            return JsonResponse({"error": f"Usuario con ID:{usuario_id} no encontrado"}, status=404)
            
    return JsonResponse({"error": "El endpoint que quieres no es Permitido solo DELETE"}, status=405)

@csrf_exempt
def delete_sala(request, sala_id : int) -> JsonResponse:
    if request.method == "DELETE":
        try:
            sala = Sala.objects.get(id = sala_id)
            sala.delete()
            return JsonResponse({
                "mensaje" : f"El usuario con id {sala_id} ha sido eliminado correctamente "})
            
        except Sala.DoesNotExist:
            return JsonResponse({"error": f"Sala con ID:{sala_id} no encontrado"}, status=404)
            
    return JsonResponse({"error": "El endpoint que quieres no es Permitido solo DELETE"}, status=405)


@csrf_exempt
def delete_monitor(request, monitor_id : int) -> JsonResponse:
    if request.method == "DELETE":
        try:
            monitor = Monitor.objects.get(id = monitor_id)
            monitor.delete()
            return JsonResponse({
                "mensaje" : f"El monitor con id {monitor_id} ha sido eliminado correctamente "})
            
        except Monitor.DoesNotExist:
            return JsonResponse({"error": f"Monitor con ID:{monitor_id} no encontrado"}, status=404)
            
    return JsonResponse({"error": "El endpoint que quieres no es Permitido solo DELETE"}, status=405)



@csrf_exempt
def delete_responsable_sala(request, responsable_sala_id : int) -> JsonResponse:
    if request.method == "DELETE":
        try:
            responsable_sala = ResponsableSala.objects.get(id = responsable_sala_id)
            responsable_sala.delete()
            return JsonResponse({
                "mensaje" : f"El responsable_sala con id {responsable_sala_id} ha sido eliminado correctamente "})
            
        except ResponsableSala.DoesNotExist:
            return JsonResponse({"error": f"ResponsableSala con ID:{responsable_sala_id} no encontrado"}, status=404)
            
    return JsonResponse({"error": "El endpoint que quieres no es Permitido solo DELETE"}, status=405)



@csrf_exempt
def delete_actividad(request, actividad_id : int) -> JsonResponse:
    """Si borras un Monitor, se borran sus actividades.
        Si borras una Sala, se borran sus actividades.
        Pero si borras una Actividad, no se borra ni el monitor ni la sala.
    """
    if request.method == "DELETE":
        try:
            actividad = Actividad.objects.get(id = actividad_id)
            actividad.delete()
            return JsonResponse({
                "mensaje" : f"El actividad con id {actividad_id} ha sido eliminado correctamente "})
            
        except Actividad.DoesNotExist:
            return JsonResponse({"error": f"Actividad con ID:{actividad_id} no encontrada"}, status=404)
            
    return JsonResponse({"error": "El endpoint que quieres no es Permitido solo DELETE"}, status=405)

