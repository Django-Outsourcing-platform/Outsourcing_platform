# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2020-03-01 11:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20200225_1909'),
        ('outsource', '0003_auto_20191221_1545'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jingbiao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_id', models.IntegerField(default=0, verbose_name='竞标状态')),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='outsource.Projects')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
        ),
    ]
