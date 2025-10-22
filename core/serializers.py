from rest_framework import serializers
from .models import Servicio, Contacto


class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = ['id', 'titulo', 'descripcion', 'imagen']


class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        fields = ['id', 'nombre', 'email', 'mensaje', 'empresa', 'telefono']
