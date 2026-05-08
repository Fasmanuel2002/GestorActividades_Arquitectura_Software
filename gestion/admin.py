from django.contrib import admin
from .models import Usuario, Sala, Monitor, ResponsableSala, Actividad


admin.site.register(Usuario)
admin.site.register(Sala)
admin.site.register(Monitor)
admin.site.register(ResponsableSala)
admin.site.register(Actividad)
