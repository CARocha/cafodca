# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-05 15:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendas', '0003_auto_20180905_0921'),
    ]

    operations = [
        migrations.AddField(
            model_name='agendas',
            name='lugar',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]