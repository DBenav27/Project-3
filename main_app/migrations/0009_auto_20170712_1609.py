# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-12 16:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_auto_20170712_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treasure',
            name='about',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AlterField(
            model_name='treasure',
            name='breed',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AlterField(
            model_name='treasure',
            name='dog',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]
