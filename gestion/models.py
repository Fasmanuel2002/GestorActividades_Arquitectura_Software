from django.db import models



class Actividad(models.Model):
    nombre_actividad = models.CharField(min_length=3, max_length=50)
    tipo_actividad = models.CharField(min_length=3, max_length=50)
    horario_actividad = models.CharField(min_length=3, max_length=50)
    descripcion_actividad = models.CharField(min_length=3, max_length=200)
    duracion_actividad = models.CharField(min_length=3, max_length=50)
    plazas_disponibles = models.PositiveIntegerField()
    
    monitor_actividad = models.ForeignKey(
        "Monitor",
        on_delete=models.CASCADE,
        related_name="actividades"
        )
    

class Usuario(models.Model):
    nombre_usuario = models.CharField(min_length=3, max_length=50)
    edad_usuario = models.PositiveIntegerField(max_length=3)
    email_usuario = models.EmailField(min_length=3, max_length=50)
    telefono_usuario = models.CharField(min_length=7, max_length=10)
    
    def __str__(self):
        return self.nombre_usuario
    

class Monitor(models.Model):
    nombre = models.CharField(min_length=3, max_length=50)
    especializacion = models.CharField(min_length=3, max_length=50)
    
    
    @property
    def actividades_asignadas(self):
        ...
        
