# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-05 14:24
from __future__ import unicode_literals

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notas',
            name='foto',
            field=sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to='notas/'),
        ),
    ]
