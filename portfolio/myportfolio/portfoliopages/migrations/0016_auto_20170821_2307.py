# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-21 23:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfoliopages', '0015_project_demo_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
