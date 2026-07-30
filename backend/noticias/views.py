from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Noticia
from .serializers import NoticiaListSerializer, NoticiaDetailSerializer
from .permissions import EsAdminOSoloLectura


class NoticiaViewSet(viewsets.ModelViewSet):
    permission_classes = [EsAdminOSoloLectura]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['titulo', 'resumen', 'contenido']
    ordering_fields = ['fecha_publicacion', 'fecha_creacion']
    lookup_field = 'slug'

    def get_queryset(self):
        qs = Noticia.objects.all()
        # Un visitante no autenticado solo ve noticias publicadas.
        # El admin autenticado ve todo (incluyendo borradores).
        if not self.request.user.is_authenticated:
            qs = qs.filter(estado=Noticia.Estado.PUBLICADO)
        return qs

    def get_serializer_class(self):
        # Público (sin autenticar) en el listado: serializer liviano
        if self.action == 'list' and not self.request.user.is_authenticated:
            return NoticiaListSerializer
        # Admin autenticado (listado o cualquier otra acción): serializer completo
        return NoticiaDetailSerializer
