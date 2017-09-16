# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-16 16:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170916_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 16, 16, 41, 53, 959655, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 16, 16, 41, 53, 958637, tzinfo=utc)),
        ),
    ]