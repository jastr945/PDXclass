# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-23 05:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfoliopages', '0010_project_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
