# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-04-22 16:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotosportada',
            name='orden',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
