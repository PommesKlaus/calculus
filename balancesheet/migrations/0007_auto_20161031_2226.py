# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-31 21:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('balancesheet', '0006_auto_20161031_2143'),
    ]

    operations = [
        migrations.AddField(
            model_name='difference',
            name='oci_movement',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=13),
        ),
        migrations.AddField(
            model_name='difference',
            name='oci_true_up',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=13),
        ),
        migrations.AlterField(
            model_name='difference',
            name='name',
            field=models.CharField(default='2016-10-31 22:26:18.472275', max_length=160),
        ),
    ]
