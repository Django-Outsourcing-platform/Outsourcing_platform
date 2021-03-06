# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2020-02-12 11:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0003_auto_20191218_1533'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='发帖标题')),
                ('content', models.CharField(max_length=500, verbose_name='发帖内容')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
            options={
                'verbose_name': '发布新帖表',
                'verbose_name_plural': '发布新帖表',
                'db_table': 'questions',
            },
        ),
    ]
