from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .models import Usuario, Sala, Monitor, ResponsableSala, Actividad


def inicio(request):
    return render(request, "gestion/inicio.html")
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


"""
POST ENDPOINTS
"""

# Endpoint para registrar un usuario a través de una solicitud POST con JSON
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


#/ Endpoint para crear un usuario a través de un formulario HTML
def crear_usuario_formulario(request):
    if request.method == "POST":
        Usuario.objects.create(
            nombre_usuario=request.POST["nombre_usuario"],
            edad_usuario=request.POST["edad_usuario"],
            email_usuario=request.POST["email_usuario"],
            telefono_usuario=request.POST["telefono_usuario"]
        )

        return redirect("list_usuarios_inscritos")

    return render(request, "gestion/POST/formulario_usuario.html")


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

#/ Endpoint para crear un sala a través de un formulario HTML
def registrar_sala_formulario(request):
    if request.method == "POST":
        Sala.objects.create(
            nombre_sala=request.POST["nombre_sala"],
            capacidad_sala=request.POST["capacidad_sala"],
            ubicacion_sala=request.POST["ubicacion_sala"]
        )
        return redirect("crear_sala_formulario")
    return render(request, "gestion/POST/formulario_sala.html")


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


# Endpoint para crear un monitor a través de un formulario HTML
def registrar_monitor_formulario(request):
    if request.method == "POST":
        Monitor.objects.create(
            nombre=request.POST["nombre"],
            especializacion=request.POST["especializacion"]
        )
        return redirect("lista_monitores")
    return render(request, "gestion/POST/formulario_monitor.html")

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

# Endpoint para crear un responsable de sala a través de un formulario HTML
def registrar_responsable_sala_formulario(request):
    if request.method == "POST":
        sala = Sala.objects.get(id=request.POST["sala_id"])
        ResponsableSala.objects.create(
            nombre_responsable=request.POST["nombre_responsable"],
            telefono_responsable=request.POST["telefono_responsable"],
            email_responsable=request.POST["email_responsable"],
            sala=sala
        )
        return redirect("crear_responsable_sala_formulario")
    salas = Sala.objects.all()
    return render(request, "gestion/POST/formulario_responsable_sala.html", {"salas": salas})


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


# Endpoint para crear una actividad a través de un formulario HTML
def registrar_actividad_formulario(request):
    if request.method == "POST":
        monitor = Monitor.objects.get(id=request.POST["monitor_actividad_id"])
        sala_principal = Sala.objects.get(id=request.POST["sala_principal_id"])
        Actividad.objects.create(
            nombre_actividad=request.POST["nombre_actividad"],
            tipo_actividad=request.POST["tipo_actividad"],
            horario_actividad=request.POST["horario_actividad"],
            descripcion_actividad=request.POST["descripcion_actividad"],
            duracion_actividad=request.POST["duracion_actividad"],
            plazas_disponibles=request.POST["plazas_disponibles"],
            monitor_actividad=monitor,
            sala_principal=sala_principal
        )
        return redirect("crear_actividad_formulario")
    monitores = Monitor.objects.all()
    salas = Sala.objects.all()
    return render(request, "gestion/POST/formulario_actividad.html", {"monitores": monitores, "salas": salas})





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

