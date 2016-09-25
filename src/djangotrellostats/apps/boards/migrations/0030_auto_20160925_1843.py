# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-25 16:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0029_auto_20160925_1842'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='card',
            index_together=set([('board', 'creation_datetime'), ('board', 'creation_datetime', 'list'), ('board', 'list', 'position')]),
        ),
    ]
