# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-11 16:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20170711_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treasure',
            name='image',
            field=models.ImageField(default=b'media/default.png', upload_to=b'treasure_images'),
        ),
    ]
