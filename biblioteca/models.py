# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from contrapartes.models import Contraparte
from sorl.thumbnail import ImageField

# Create your models here.

class Tematicas(models.Model):
    nombre = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, editable=False)

    def __unicode__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        self.slug = (slugify(self.nombre))
        super(Tematicas, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Tematica'
        verbose_name_plural = 'Tematicas'

class Publicaciones(models.Model):
    titulo = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, editable=False)
    fecha = models.DateTimeField(auto_now=True)
    imagen_portada = ImageField(upload_to='foto/publicaciones/', null=True, blank=True)
    autor = models.CharField(verbose_name='Autor de la publicación', max_length=250)
    coparte = models.ForeignKey(Contraparte)
    descripcion = models.TextField('Descripción')
    tematicas = models.ManyToManyField(Tematicas)
    adjunto = models.FileField(upload_to='biblioteca/', null=True, blank=True)

    user = models.ForeignKey(User)


    def __unicode__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        self.slug = (slugify(self.titulo))
        super(Publicaciones, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones'

    @models.permalink
    def get_absolute_url(self):
        return ("publicacion-detalle", [self.slug,])

    def todas_tematicas(self):
        all_temas = ', '.join([obj.nombre for obj in self.tematicas.all()])
        return all_temas

    def all_tematicas(self):
        all_temas = ' '.join([slugify(obj.nombre) for obj in self.tematicas.all()])
        return all_temas
