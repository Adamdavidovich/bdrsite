# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-30 22:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='querydropdown',
            name='query',
            field=models.CharField(choices=[('1', 'Relative Abundance/Resistance of Plated Samples'), ('2', 'Other')], max_length=200),
        ),
    ]
