# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-25 20:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orz_app', '0004_auto_20171026_0442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='blog_comment',
            field=models.TextField(),
        ),
    ]
