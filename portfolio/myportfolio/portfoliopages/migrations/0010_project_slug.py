# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-21 22:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfoliopages', '0009_profilepic'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='slug',
            field=models.SlugField(default='string'),
        ),
    ]
