# -*- coding: utf-8 -*-
from django.db import models
from user.models import User


# Create your models here.

# 项目发布表
class PublishProject(models.Model):
    class_id = models.IntegerField(verbose_name='项目类别')
    project_name = models.CharField(max_length=100, verbose_name="项目名称")
    post_datetime = models.DateTimeField(auto_now_add=True, verbose_name="发包时间")
    end_datetime = models.DateTimeField(auto_now=True, verbose_name="截止时间")
    kind = models.CharField(choices=((u'Android', u'Android'),
                                     (u'Ios', u'Ios'),
                                     (u'PC', u'PC网站'),
                                     (u'wechart', u'微信端开发'),
                                     (u'other', u'其它'),
                                     ), max_length=50, default="other", verbose_name="类型")
    cycles = models.IntegerField(verbose_name="开发周期", null=True)
    budget = models.CharField(max_length=20, verbose_name="预算")
    project_descrption = models.TextField(max_length=300, default="项目描述", verbose_name="项目描述")
    # compete_state = models.BooleanField(default=0, verbose_name="竞标状态", null=True)
    # 外键关联 用户表(onetomany)
    user = models.ForeignKey(User)

    # category = models.ForeignKey(Category, blank=True, null=True, verbose_name='分类')
    # tag = models.ManyToManyField(Tag, verbose_name='标签')

    class Meta:
        db_table = "publish"
        verbose_name = "项目发布表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.project_name)
