# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-12-07 03:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '用户信息表', 'verbose_name_plural': '用户信息表'},
        ),
        migrations.AlterModelTable(
            name='user',
            table='user',
        ),
    ]
