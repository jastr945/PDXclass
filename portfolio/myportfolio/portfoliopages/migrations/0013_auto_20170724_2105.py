# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 21:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfoliopages', '0012_auto_20170724_0004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectpage',
            name='project',
        ),
        migrations.AlterField(
            model_name='bio',
            name='text',
            field=models.TextField(max_length=255),
        ),
        migrations.DeleteModel(
            name='ProjectPage',
        ),
    ]