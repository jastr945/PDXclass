# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-21 22:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfoliopages', '0014_auto_20170724_2108'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='demo_link',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]