# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 21:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfoliopages', '0013_auto_20170724_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(max_length=255),
        ),
    ]
