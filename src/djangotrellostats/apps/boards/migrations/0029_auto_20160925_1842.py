# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-25 16:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0028_auto_20160925_1809'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='label',
            options={'verbose_name': 'label', 'verbose_name_plural': 'labels'},
        ),
        migrations.AlterIndexTogether(
            name='label',
            index_together=set([('board', 'name', 'color')]),
        ),
    ]
