# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-08 19:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FileHandler', '0006_auto_20170108_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='exposition_time',
            field=models.SmallIntegerField(default=2),
        ),
    ]
