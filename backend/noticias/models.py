from django.db import models
from django.utils.text import slugify


class Noticia(models.Model):
    class Estado(models.TextChoices):
        BORRADOR = 'borrador', 'Borrador'
        PUBLICADO = 'publicado', 'Publicado'

    titulo = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    resumen = models.CharField(max_length=300)
    contenido = models.TextField(help_text="Contenido en formato HTML")
    imagen_portada = models.ImageField(upload_to='noticias/')
    imagen_portada_alt = models.CharField(max_length=200, blank=True)
    estado = models.CharField(
        max_length=10,
        choices=Estado.choices,
        default=Estado.BORRADOR,
    )
    fecha_publicacion = models.DateTimeField(null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"
        ordering = ['-fecha_publicacion', '-fecha_creacion']

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        # Autogenera el slug a partir del título si no existe
        if not self.slug:
            base_slug = slugify(self.titulo)
            slug = base_slug
            contador = 1
            while Noticia.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{contador}"
                contador += 1
            self.slug = slug

        # Marca la fecha de publicación automáticamente al pasar a "publicado"
        if self.estado == self.Estado.PUBLICADO and self.fecha_publicacion is None:
            from django.utils import timezone
            self.fecha_publicacion = timezone.now()

        super().save(*args, **kwargs)
