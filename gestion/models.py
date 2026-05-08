from django.db import models

class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=50)
    edad_usuario = models.PositiveIntegerField()
    email_usuario = models.EmailField(max_length=100)
    telefono_usuario = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre_usuario


class Sala(models.Model):
    nombre_sala = models.CharField(max_length=50)
    capacidad_sala = models.PositiveIntegerField()
    ubicacion_sala = models.CharField(max_length=50)

    
    def __str__(self):
        return self.nombre_sala
    

    
class Monitor(models.Model):
    nombre = models.CharField(max_length=50)
    especializacion = models.CharField(max_length=50)
    
    @property
    def numero_actividades_asignadas(self):
        return self.actividades.count()
        
    def __str__(self):
        return f"{self.nombre} Especializado en: {self.especializacion} Tiene asignada esta cantidad de actividades: {self.numero_actividades_asignadas}"


class ResponsableSala(models.Model):
    nombre_responsable = models.CharField(max_length=50)
    telefono_responsable = models.CharField(max_length=15)
    email_responsable = models.EmailField(max_length=100)

    sala = models.OneToOneField(
        Sala,
        on_delete=models.CASCADE,
        related_name="responsable_sala")
    
    def __str__(self):
        return self.nombre_responsable
        
    
    
class Actividad(models.Model):
    nombre_actividad = models.CharField(max_length=50)
    tipo_actividad = models.CharField(max_length=50)
    horario_actividad = models.CharField(max_length=50)
    descripcion_actividad = models.TextField(max_length=200)
    duracion_actividad = models.PositiveIntegerField()
    plazas_disponibles = models.PositiveIntegerField()
    
    monitor_actividad = models.ForeignKey(
        Monitor,
        on_delete=models.CASCADE,
        related_name="actividades"
        )
    
    sala_principal = models.ForeignKey(Sala, on_delete=models.CASCADE, related_name="actividades_sala_principal")

    salas_secundarias = models.ManyToManyField(
        Sala,
        related_name="actividades_sala_secundaria",
        blank=True
    )
    
    usuarios_inscritos_actividad = models.ManyToManyField(
        Usuario,
        through='UsuariosActividad',
        related_name="actividades_inscritas",
        blank=True
    )
    
    def __str__(self):
        return self.nombre_actividad

    


class UsuariosActividad(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="usuario_actividades")
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, related_name="actividades_usuario")
    
    def __str__(self):
        return f"{self.usuario.nombre_usuario} inscrito en {self.actividad.nombre_actividad}"