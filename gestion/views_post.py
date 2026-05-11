from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Usuario, Sala, Monitor, ResponsableSala, Actividad, UsuariosActividad


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




def inscribir_usuario_actividad_formulario(request, actividad_id : int) -> render:
    actividad = Actividad.objects.get(id = actividad_id)
    if request.method == "POST":
        usuario_inscribir = Usuario.objects.get(id=request.POST["usuario_id"])
        UsuariosActividad.objects.create(
            usuario = usuario_inscribir,
            actividad = actividad
        )
        return redirect("inscribir_usuario_actividad_formulario", actividad_id=actividad.id)
    usuarios = Usuario.objects.all()
    
    return render(request, "gestion/Inscripciones/formulario_usuario_actividad.html", {"usuarios": usuarios, "actividad": actividad})


@csrf_exempt
def eliminar_inscripcion_actividad(request, actividad_id, usuario_id):
    if request.method == 'POST':
        try:
            actividad = Actividad.objects.get(id=actividad_id)
            usuario = Usuario.objects.get(id=usuario_id)
            inscripcion = UsuariosActividad.objects.get(
                actividad=actividad,
                usuario=usuario
            )
            inscripcion.delete()
            return JsonResponse({"mensaje": "Inscripción eliminada con éxito"})
        except Actividad.DoesNotExist:
            return JsonResponse({"error": "Actividad no encontrada"}, status=404)
        except Usuario.DoesNotExist:
            return JsonResponse({"error": "Usuario no encontrado"}, status=404)
        except UsuariosActividad.DoesNotExist:
            return JsonResponse({"error": "Inscripción no encontrada"}, status=404)
    return JsonResponse({"error": "Método no permitido"}, status=405)