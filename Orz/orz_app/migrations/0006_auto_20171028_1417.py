# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-28 06:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orz_app', '0005_auto_20171026_0445'),
    ]

    operations = [
        migrations.RenameField(
            model_name='classification',
            old_name='classifiication_name',
            new_name='classification_name',
        ),
        migrations.AddField(
            model_name='classification',
            name='english_name',
            field=models.CharField(default='abc', max_length=64),
        ),
    ]