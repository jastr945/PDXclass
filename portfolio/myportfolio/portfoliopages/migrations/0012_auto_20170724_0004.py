# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 00:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfoliopages', '0011_auto_20170723_0549'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AddField(
            model_name='projectpage',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfoliopages.Project'),
        ),
    ]
