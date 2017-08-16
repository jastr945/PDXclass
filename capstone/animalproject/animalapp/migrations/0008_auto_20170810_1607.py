# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-10 23:07
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('animalapp', '0007_auto_20170810_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='home',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('cats', 'cats'), ('dogs', 'dogs'), ('other pets', 'other pets'), ('young children', 'young children')], default='', max_length=255, verbose_name='Prefers a home without (optional)'),
        ),
    ]