# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-22 03:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20180111_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='category',
            field=models.CharField(default='default', max_length=128),
        ),
    ]
