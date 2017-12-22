# -*- coding: utf-8 -*-

from django.db import models


# Create your models here.
class Ops_record(models.Model):
    """操作记录"""

    ip = models.CharField(u"IP地址", max_length=30)
    app_id = models.CharField(u"业务ID", max_length=10)
    username = models.CharField(u"操作用户", max_length=64)
    result = models.CharField(u"操作结果", max_length=256)
    def __unicode__(self):
        return self.username

    class Meta:
        verbose_name = u"操作记录"
        verbose_name_plural = u"操作记录"
        app_label = "xiaobo"
