# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-10 17:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='treasure',
            old_name='value',
            new_name='age',
        ),
        migrations.RenameField(
            model_name='treasure',
            old_name='material',
            new_name='gender',
        ),
    ]
