# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-28 18:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('id_number', models.IntegerField()),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], default='', max_length=20)),
                ('breed', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=50)),
                ('surgery', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='', max_length=20)),
                ('location', models.CharField(max_length=50)),
                ('intake_date', models.DateField()),
                ('status', models.CharField(choices=[('av', 'available'), ('temp', 'temporarily unavailable'), ('oh', 'on hold'), ('adt', 'ADOPTED')], default='av', max_length=20)),
                ('personality', models.CharField(max_length=255)),
                ('slug', models.SlugField(default='')),
            ],
        ),
    ]
