# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-03 23:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0008_auto_20161211_1901'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardreview',
            name='description',
            field=models.TextField(blank=True, default='', verbose_name='Description of the review'),
        ),
    ]
