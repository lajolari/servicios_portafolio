from rest_framework import serializers
from contacto.models import Mensaje, LANGUAGE_CHOICES, STYLE_CHOICES


class MensajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mensaje
        fields = ['id', 'nombre', 'correo', 'telefono', 'mensaje', 'linenos', 'language', 'style']