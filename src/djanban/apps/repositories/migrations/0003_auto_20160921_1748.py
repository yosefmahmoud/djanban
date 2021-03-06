# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-21 15:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repositories', '0002_auto_20160911_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='gitlabrepository',
            name='ci_token',
            field=models.CharField(default='', help_text='CI token used to clone and checkout the repository', max_length=128, verbose_name='CI token for the repository'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gitlabrepository',
            name='project_userspace',
            field=models.CharField(default='', max_length=128, verbose_name='Project userspace'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='gitlabrepository',
            name='project_name',
            field=models.CharField(max_length=128, verbose_name='Project name'),
        ),
    ]
