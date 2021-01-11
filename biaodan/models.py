# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Clazz(models.Model):
    cno = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=20,verbose_name=u'班级：')

    def __unicode__(self):
        return u'Clazz:%s' % self.cname


class Stu(models.Model):
    sno = models.AutoField(primary_key=True)
    sname = models.CharField(max_length=30,verbose_name=u'姓名：')
    password = models.CharField(max_length=30)
    clazz = models.ForeignKey(Clazz, on_delete=models.CASCADE)

    def __unicode__(self):
        return u'Stu:%s,%s' % (self.sno, self.sname)
