# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-20 21:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfoliopages', '0007_bio'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bio',
            options={'verbose_name_plural': 'Bio'},
        ),
        migrations.AddField(
            model_name='project',
            name='readme_link',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_link',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]