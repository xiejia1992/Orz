# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-28 06:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orz_app', '0006_auto_20171028_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classification',
            name='english_name',
            field=models.CharField(max_length=64),
        ),
    ]