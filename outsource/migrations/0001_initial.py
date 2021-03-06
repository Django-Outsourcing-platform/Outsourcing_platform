# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-12-17 13:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Developers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='真实姓名')),
                ('nickname', models.CharField(max_length=50, verbose_name='昵称')),
                ('email', models.EmailField(max_length=50, verbose_name='邮箱')),
                ('phone', models.CharField(max_length=50, verbose_name='手机号')),
                ('price_min', models.CharField(max_length=50, verbose_name='最低价')),
                ('price_max', models.CharField(max_length=50, verbose_name='最高价')),
                ('work_status', models.CharField(max_length=50, verbose_name='工作状态')),
                ('work_direction', models.CharField(max_length=50, verbose_name='职业方向')),
                ('language_direction', models.CharField(max_length=50, verbose_name='语言方向')),
                ('sex', models.CharField(max_length=50, verbose_name='工作状态')),
                ('person_introduce', models.TextField(max_length=500, verbose_name='个人介绍')),
                ('work_experience', models.TextField(max_length=500, verbose_name='工作经历')),
                ('project_works', models.TextField(max_length=500, verbose_name='开发作品')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
            options={
                'verbose_name': '开发者信息表',
                'verbose_name_plural': '开发者信息表',
                'db_table': 'user_dev',
            },
        ),
        migrations.CreateModel(
            name='KindChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind_name', models.CharField(default='其它分类', max_length=30, verbose_name='项目类别')),
            ],
            options={
                'verbose_name': '项目类别选择表',
                'verbose_name_plural': '项目类别选择表',
                'db_table': 'kind_choice',
            },
        ),
        migrations.CreateModel(
            name='LanguageChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_name', models.CharField(default='暂无', max_length=30, verbose_name='开发语言')),
            ],
            options={
                'verbose_name': '开发语言选择表',
                'verbose_name_plural': '开发语言选择表',
                'db_table': 'language_choice',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_detail_url', models.URLField(default='#', verbose_name='详情页链接')),
                ('news_title', models.CharField(max_length=200, verbose_name='新闻标题')),
                ('news_tip', models.CharField(max_length=200, verbose_name='文章摘要')),
                ('image_url', models.ImageField(upload_to='', verbose_name='图片路径')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '新闻列表页',
                'verbose_name_plural': '新闻列表页',
                'db_table': 'news',
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100, verbose_name='项目名称')),
                ('kind', models.CharField(default=8, max_length=100, verbose_name='项目类别')),
                ('budget', models.CharField(max_length=20, null=True, verbose_name='预算')),
                ('language', models.CharField(default=9, max_length=100, verbose_name='开发语言')),
                ('cycles', models.IntegerField(null=True, verbose_name='开发周期')),
                ('project_desc', models.TextField(default='项目描述', max_length=300, verbose_name='项目描述')),
                ('post_datetime', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
                ('views', models.IntegerField(default=0, verbose_name='浏览数量')),
                ('is_Active', models.BooleanField(default=True, verbose_name='项目状态')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
            options={
                'verbose_name': '项目表',
                'verbose_name_plural': '项目表',
                'db_table': 'projects',
            },
        ),
    ]
