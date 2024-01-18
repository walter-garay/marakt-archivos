from django.shortcuts import render
from rest_framework import viewsets
from . import serializers, models
# Create your views here.

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = models.Usuario.objects.all()
    serializer_class = serializers.UsuarioSerializer

# MODULO NEGOCIO

class ArchivoViewSet(viewsets.ModelViewSet):
    queryset = models.Archivo.objects.all()
    serializer_class = serializers.ArchivoSerializer