# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-12 23:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='last_fetch_datetime',
            field=models.DateTimeField(default=None, null=True, verbose_name='Last fetch datetime'),
        ),
    ]