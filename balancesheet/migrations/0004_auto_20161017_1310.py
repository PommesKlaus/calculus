# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-17 11:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('balancesheet', '0003_auto_20161014_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='difference',
            name='name',
            field=models.CharField(default='2016-10-17 13:10:16.662900', max_length=160),
        ),
    ]
