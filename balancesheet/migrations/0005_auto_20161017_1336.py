# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-17 11:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('balancesheet', '0004_auto_20161017_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bslineitem',
            name='name',
            field=models.CharField(max_length=160, verbose_name='Bezeichnung'),
        ),
        migrations.AlterField(
            model_name='difference',
            name='name',
            field=models.CharField(default='2016-10-17 13:36:22.763658', max_length=160),
        ),
    ]
