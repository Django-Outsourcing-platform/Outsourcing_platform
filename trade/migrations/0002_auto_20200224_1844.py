# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2020-02-24 10:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': '项目分享', 'verbose_name_plural': '项目分享'},
        ),
        migrations.AddField(
            model_name='project',
            name='image_url',
            field=models.ImageField(default='', upload_to='project_share', verbose_name='图片路径'),
        ),
    ]