from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombres = models.CharField(max_length=64)
    apellidos = models.CharField(max_length=64)
    email = models.EmailField(unique=True, blank=False, null=False)  # El argumento blank=False hace que el campo sea obligatorio
    password = models.CharField(max_length=128, blank=False, null=False)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nombres} {self.apellidos}'
    
class Archivo(models.Model):
    nombre = models.CharField(max_length=64)
    fecha_subida = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    archivo = models.FileField(upload_to='archivos/')

    def __str__(self):
        return f'{self.nombre}'