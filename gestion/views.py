from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .models import Usuario, Sala, Monitor, ResponsableSala, Actividad


def inicio(request):
    return render(request, "gestion/inicio.html")
