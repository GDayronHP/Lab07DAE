from django.db import models

class Usuario(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]
    
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100, default='')  
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=True, null=True, default='O')  
    contraseña = models.CharField(max_length=128)  

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"  


class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha = models.DateField()
    lugar = models.CharField(max_length=255)
    organizador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='eventos_organizados')
    capacidad = models.PositiveIntegerField()

    def __str__(self):
        return self.titulo


class RegistroEvento(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='registros')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='registros_evento')
    fecha_registro = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('evento', 'usuario')

    def __str__(self):
        return f"{self.usuario} registrado en {self.evento}"
