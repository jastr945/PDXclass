# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-08 22:36
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('animalapp', '0002_auto_20170808_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='cat_personality',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('playful', 'playful'), ('sociable and outgoing', 'sociable and outgoing'), ('a bit shy in the shelter environment', 'a bit shy in the shelter environment'), ('loves to be around people', 'loves to be around people')], default='', max_length=92),
        ),
        migrations.AlterField(
            model_name='dog',
            name='dog_personality',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('playful', 'playful'), ('sociable and outgoing', 'sociable and outgoing'), ('profoundly loyal', 'profoundly loyal')], default='', max_length=46),
        ),
    ]