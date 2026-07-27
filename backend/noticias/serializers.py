from rest_framework import serializers
from .models import Noticia

class NoticiaListSerializer(serializers.ModelSerializer):
    """Para el feed: solo lo necesario para mostrar tarjetas."""
    class Meta:
        model = Noticia
        fields = [
            'id', 'titulo', 'slug', 'resumen',
            'imagen_portada', 'imagen_portada_alt',
            'fecha_publicacion',
        ]


class NoticiaDetailSerializer(serializers.ModelSerializer):
    """Para el detalle público y para el panel de admin (CRUD completo)."""

    class Meta:
        model = Noticia
        fields = [
            'id', 'titulo', 'slug', 'resumen', 'contenido',
            'imagen_portada', 'imagen_portada_alt',
            'estado', 'fecha_publicacion',
            'fecha_creacion', 'fecha_actualizacion',
        ]
        read_only_fields = ['slug', 'fecha_publicacion', 'fecha_creacion', 'fecha_actualizacion']