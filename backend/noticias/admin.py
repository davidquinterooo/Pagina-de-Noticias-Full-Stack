from django.contrib import admin
from django.utils.html import format_html
from .models import Noticia


@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'estado', 'fecha_publicacion', 'fecha_actualizacion', 'vista_previa_imagen')
    list_filter = ('estado',)
    search_fields = ('titulo', 'resumen', 'contenido')
    prepopulated_fields = {'slug': ('titulo',)}
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion', 'vista_previa_imagen_grande')
    ordering = ('-fecha_creacion',)
    list_per_page = 20

    fieldsets = (
        ('Contenido', {
            'fields': ('titulo', 'slug', 'resumen', 'contenido')
        }),
        ('Imagen', {
            'fields': ('imagen_portada', 'vista_previa_imagen_grande', 'imagen_portada_alt')
        }),
        ('Publicación', {
            'fields': ('estado', 'fecha_publicacion')
        }),
        ('Metadatos', {
            'fields': ('fecha_creacion', 'fecha_actualizacion'),
            'classes': ('collapse',),
        }),
    )

    def vista_previa_imagen(self, obj):
        if obj.imagen_portada:
            return format_html(
                '<img src="{}" style="height: 40px; border-radius: 4px;" />',
                obj.imagen_portada.url
            )
        return "—"
    vista_previa_imagen.short_description = "Imagen"

    def vista_previa_imagen_grande(self, obj):
        if obj.imagen_portada:
            return format_html(
                '<img src="{}" style="max-height: 200px; border-radius: 8px;" />',
                obj.imagen_portada.url
            )
        return "Aún no hay imagen"
    vista_previa_imagen_grande.short_description = "Vista previa"
# Register your models here.
