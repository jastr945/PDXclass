# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-18 22:19
from __future__ import unicode_literals

from django.db import migrations, models
import portfoliopages.models


class Migration(migrations.Migration):

    dependencies = [
        ('portfoliopages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to=portfoliopages.models.profile_upload_handler),
        ),
    ]
