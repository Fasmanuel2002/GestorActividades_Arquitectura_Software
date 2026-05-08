from django.shortcuts import render


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
 
