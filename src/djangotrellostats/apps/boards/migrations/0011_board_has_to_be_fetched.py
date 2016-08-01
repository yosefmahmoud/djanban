# -*- coding: utf-8 -*-
# Generated by Django 1.10rc1 on 2016-08-01 15:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0010_card_members'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='has_to_be_fetched',
            field=models.BooleanField(default=True, verbose_name='Informs if this board has to be fetched'),
        ),
    ]
