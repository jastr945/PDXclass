# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-18 22:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfoliopages', '0004_auto_20170718_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_link',
            field=models.CharField(max_length=500),
        ),
    ]
