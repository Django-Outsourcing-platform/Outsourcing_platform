# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2020-02-25 10:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0004_remove_project_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='likenum',
            options={'verbose_name': '项目点赞数', 'verbose_name_plural': '项目点赞数'},
        ),
        migrations.AlterModelOptions(
            name='likeuser',
            options={'verbose_name': '项目点赞用户', 'verbose_name_plural': '项目点赞用户'},
        ),
        migrations.AlterModelTable(
            name='likenum',
            table='trade_likenum',
        ),
        migrations.AlterModelTable(
            name='likeuser',
            table='trade_likeuser',
        ),
    ]