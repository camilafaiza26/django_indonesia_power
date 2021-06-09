# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-10-27 13:25
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PLTU',
            fields=[
                ('id_pltu', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(99999)])),
                ('nama_pltu', models.CharField(blank=True, max_length=50, null=True)),
                ('lokasi_pltu', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'dim_pltu',
            },
        ),
        migrations.CreateModel(
            name='Sumbertambang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_sumber_tambang', models.CharField(blank=True, max_length=100, null=True)),
                ('nama_sumber_tambang', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'db_table': 'dim_sumbertambang',
            },
        ),
        migrations.CreateModel(
            name='Waktu',
            fields=[
                ('id_waktu', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(99999)])),
                ('waktu_mulai', models.CharField(blank=True, max_length=50, null=True)),
                ('waktu_selesai', models.CharField(blank=True, max_length=100, null=True)),
                ('triwulan', models.IntegerField(validators=[django.core.validators.MaxValueValidator(99999)])),
            ],
            options={
                'db_table': 'dim_waktu',
            },
        ),
    ]