# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-09 17:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


def assign_trello_credentials(apps, schema_editor):
    Member = apps.get_model("members", "Member")
    TrelloMemberProfile = apps.get_model("members", "TrelloMemberProfile")
    for member in Member.objects.all():
        trello_member_profile = TrelloMemberProfile(
            api_key=member.api_key,
            api_secret=member.api_secret,
            token=member.token,
            token_secret=member.token_secret,
            trello_id=member.uuid,
            username=member.trello_username,
            initials=member.initials,
            member=member
        )
        trello_member_profile.save()


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0010_memberrole'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrelloMemberProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_key', models.CharField(blank=True, default=None, max_length=128, null=True, verbose_name='Trello API key')),
                ('api_secret', models.CharField(blank=True, default=None, max_length=128, null=True, verbose_name='Trello API secret')),
                ('token', models.CharField(blank=True, default=None, max_length=128, null=True, verbose_name='Trello token')),
                ('token_secret', models.CharField(blank=True, default=None, max_length=128, null=True, verbose_name='Trello token secret')),
                ('trello_id', models.CharField(max_length=128, unique=True, verbose_name='Trello member id')),
                ('username', models.CharField(max_length=128, verbose_name='Trello username')),
                ('initials', models.CharField(max_length=8, verbose_name='User initials in Trello')),
                ('member', models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='member', to='members.Member', verbose_name='Associated member')),
            ],
        ),
        migrations.RunPython(assign_trello_credentials)
    ]
