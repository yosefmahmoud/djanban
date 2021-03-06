# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 09:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multiboards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='multiboard',
            name='show_after_development_in_review_tasks',
            field=models.BooleanField(default=True, help_text="This multiboard will show the in 'after development (in review)' tasks of its boards", verbose_name="Show 'after development (in review)' tasks"),
        ),
        migrations.AddField(
            model_name='multiboard',
            name='show_after_development_waiting_release_tasks',
            field=models.BooleanField(default=False, help_text="This multiboard will show the in 'after development (waiting release)' tasks of its boards", verbose_name="Show 'after development (waiting release)' tasks"),
        ),
        migrations.AddField(
            model_name='multiboard',
            name='show_backlog_tasks',
            field=models.BooleanField(default=True, help_text='This multiboard will show the backlog tasks of its boards', verbose_name="Show 'backlog' tasks"),
        ),
        migrations.AddField(
            model_name='multiboard',
            name='show_development_tasks',
            field=models.BooleanField(default=True, help_text="This multiboard will show the in 'development' tasks of its boards", verbose_name="Show 'in development' tasks"),
        ),
        migrations.AddField(
            model_name='multiboard',
            name='show_done_tasks',
            field=models.BooleanField(default=False, help_text='This multiboard will show the done tasks of its boards', verbose_name="Show 'done' tasks"),
        ),
        migrations.AddField(
            model_name='multiboard',
            name='show_in_index',
            field=models.BooleanField(default=False, help_text='Multiboards shown in index will be show to help users track pending tasks', verbose_name='This multiboard will be shown in index'),
        ),
        migrations.AddField(
            model_name='multiboard',
            name='show_ready_to_develop_tasks',
            field=models.BooleanField(default=True, help_text="This multiboard will show the 'ready to develop' tasks of its boards", verbose_name="Show 'ready to develop' tasks"),
        ),
        migrations.AlterField(
            model_name='multiboard',
            name='order',
            field=models.PositiveIntegerField(default=1, verbose_name='Order of this multiboard'),
        ),
    ]
