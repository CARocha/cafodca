# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-19 05:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contrapartes', '0002_redes'),
    ]

    operations = [
        migrations.AddField(
            model_name='contraparte',
            name='correo',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='mensajero',
            name='user',
            field=models.ManyToManyField(related_name='Destinatario', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='redes',
            name='opcion',
            field=models.CharField(choices=[('chrome', 'Sitio web'), ('Facebook', 'Facebook'), ('Twitter', 'Twitter'), ('Youtube', 'Youtube'), ('Google+', 'Google+'), ('Instagram', 'Instagram'), ('Linkedin', 'Linkedin'), ('Flickr', 'Flickr'), ('Pinterest', 'Pinterest'), ('Vimeo', 'Vimeo'), ('Otra', 'Otra')], max_length=25),
        ),
        migrations.AlterField(
            model_name='redes',
            name='organizacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contrapartes.Contraparte'),
        ),
    ]
