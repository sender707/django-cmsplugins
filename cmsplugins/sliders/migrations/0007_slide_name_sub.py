# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-10 13:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sliders', '0006_auto_20161206_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='name_sub',
            field=models.CharField(blank=True, default='', max_length=150, verbose_name='Subtitle'),
        ),
    ]
