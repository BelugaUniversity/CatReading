from __future__ import unicode_literals


from django.db import models


class User(models.Model):
    # 用户名
    user_name = models.CharField(max_length=14)
    # 手机号
    phone = models.CharField(max_length=11)
    