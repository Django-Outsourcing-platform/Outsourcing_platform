# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2020-02-25 11:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20191218_1533'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '用户信息', 'verbose_name_plural': '用户信息'},
        ),
    ]
