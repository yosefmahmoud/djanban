# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-04 14:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0022_auto_20160823_1808'),
    ]

    operations = [
        migrations.RenameField(
            model_name='board',
            old_name='last_activity_date',
            new_name='last_activity_datetime',
        ),
        migrations.RemoveField(
            model_name='card',
            name='last_activity_date',
        ),
        migrations.AddField(
            model_name='card',
            name='creation_datetime',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 4, 14, 42, 59, 89990, tzinfo=utc), verbose_name='Creation datetime'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='card',
            name='last_activity_datetime',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 4, 14, 43, 23, 897965, tzinfo=utc), verbose_name='Last activity datetime'),
            preserve_default=False,
        ),
    ]
