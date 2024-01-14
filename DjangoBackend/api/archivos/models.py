from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=64)
    whatsapp = models.CharField(max_length=22)

    email = models.EmailField(unique=True, blank=False)  # El argumento blank=False hace que el campo sea obligatorio
    password = models.CharField(max_length=128, blank=False, null=False)

    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    
class Archivo(models.Model):
    nombre = models.CharField(max_length=64)
    extension = models.CharField(max_length=64)
    fecha_subida = models.CharField(max_length=22)
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    archivo = models.FileField(upload_to='archivos/')

    def __str__(self):
        return f'{self.nombre}'