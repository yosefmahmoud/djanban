# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-24 15:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repositories', '0008_githubpublicrepository'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commit',
            name='commit',
            field=models.CharField(max_length=64, verbose_name='Repository commit'),
        ),
    ]
