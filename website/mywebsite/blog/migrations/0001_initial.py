# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-10-19 13:45
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data_grading',
            fields=[
                ('id_grading', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(99999999999)])),
                ('nama_pltu', models.CharField(blank=True, max_length=100, null=True)),
                ('nama_pemasok', models.CharField(blank=True, max_length=100, null=True)),
                ('gcv_realisasi', models.FloatField(blank=True, null=True)),
                ('tm_realisasi', models.FloatField(blank=True, null=True)),
                ('ts_realisasi', models.FloatField(blank=True, null=True)),
                ('ash_realisasi', models.FloatField(blank=True, null=True)),
                ('hgi_realisasi', models.FloatField(blank=True, null=True)),
                ('idt_realisasi', models.FloatField(blank=True, null=True)),
                ('pengurang_gcv', models.FloatField(blank=True, null=True)),
                ('pengurang_tm', models.FloatField(blank=True, null=True)),
                ('pengurang_ts', models.FloatField(blank=True, null=True)),
                ('pengurang_ash', models.FloatField(blank=True, null=True)),
                ('pengurang_hgi', models.FloatField(blank=True, null=True)),
                ('pengurang_idt', models.FloatField(blank=True, null=True)),
                ('persentase_realisasi', models.FloatField(blank=True, null=True)),
                ('pengurang_pasokan', models.FloatField(blank=True, null=True)),
                ('persentase_penolakan', models.FloatField(blank=True, null=True)),
                ('pengurang_batas_penolakan', models.FloatField(blank=True, null=True)),
                ('nilai_akhir', models.FloatField(blank=True, null=True)),
                ('klasifikasi', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'grading_supplier',
            },
        ),
    ]