# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2020-03-03 14:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('outsource', '0009_auto_20200303_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirm',
            name='developer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='outsource.Developers'),
        ),
        migrations.AlterField(
            model_name='confirm',
            name='project',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='outsource.Projects'),
        ),
        migrations.AlterField(
            model_name='confirm',
            name='pub_user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='user.User'),
        ),
    ]
