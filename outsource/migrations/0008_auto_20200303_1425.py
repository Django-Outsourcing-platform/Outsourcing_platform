# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2020-03-03 14:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outsource', '0007_confirm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirm',
            name='status_id',
            field=models.IntegerField(default=1, verbose_name='中标状态'),
        ),
    ]
