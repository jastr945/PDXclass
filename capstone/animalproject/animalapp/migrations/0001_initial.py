# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-01 02:13
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
                ('species', models.CharField(choices=[('dog', 'dog'), ('cat', 'cat')], default='', max_length=50)),
                ('name', models.CharField(default='', max_length=50)),
                ('id_number', models.CharField(default='', max_length=50)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], default='', max_length=20)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('surgery', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='', max_length=20, verbose_name='Spayed/neutered')),
                ('vaccine', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='yes', max_length=20, verbose_name='Vaccinated')),
                ('location', models.CharField(choices=[('OFOSA shelter', 'OFOSA shelter'), ('PetSmart Tanasbourne', 'PetSmart Tanasbourne'), ('PetSmart Wilsonville', 'PetSmart Wilsonville'), ('PetSmart Cedar Hills', 'PetSmart Cedar Hills'), ('PetSmart Hillsboro', 'PetSmart Hillsboro'), ('Foster home', 'Foster home')], default='', max_length=50)),
                ('intake_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('available', 'available'), ('temporarily unavailable', 'temporarily unavailable'), ('on hold', 'on hold'), ('ADOPTED', 'ADOPTED')], default='available', max_length=20)),
                ('home', models.CharField(blank=True, choices=[('young children', 'young children'), ('cats', 'cats'), ('dogs', 'dogs')], default='', max_length=255, verbose_name='Prefers a home without (optional)')),
                ('slug', models.SlugField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('breed', models.CharField(choices=[('Domestic shorthair/mix', 'Domestic shorthair/mix'), ('Persian', 'Persian'), ('Siamese', 'Siamese')], default='Domestic shorthair/mix', max_length=50)),
                ('color', models.CharField(choices=[('white', 'white'), ('black', 'black'), ('tabby', 'tabby'), ('seal point', 'seal point')], default='', max_length=255)),
                ('personality', models.CharField(choices=[('sociable and outgoing', 'sociable and outgoing'), ('a bit shy in the shelter environment', 'a bit shy in the shelter environment')], default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('breed', models.CharField(choices=[('Terrier/Mix', 'Terrier/Mix'), ('Chihuahua', 'Chihuahua'), ('Shepherd/Mix', 'Shepherd/Mix')], default='', max_length=50)),
                ('size', models.CharField(choices=[('small', 'small'), ('medium', 'medium'), ('large', 'large')], default='', max_length=50)),
                ('weight', models.FloatField(blank=True, default='', max_length=50, verbose_name='Specify weight (optional)')),
                ('color', models.CharField(choices=[('white', 'white'), ('black', 'black')], default='', max_length=255)),
                ('personality', models.CharField(choices=[('sociable and outgoing', 'sociable and outgoing'), ('profoundly loyal', 'profoundly loyal')], default='', max_length=255)),
            ],
        ),
    ]
