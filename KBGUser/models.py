# create by xlin 20121201
# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models

GENDER_CHOICES = (
    ('M', '男'),
    ('F', '女'),
)

PROVINCE_CHOICES = ()

class KBGUser(User):
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    mobile_phone = models.CharField(max_length=11, blank=True, verbose_name="手机")
    phone = models.CharField(max_length=11, blank=True, verbose_name='电话')
    address = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    province = models.CharField(max_length=2, choices=PROVINCE_CHOICES, blank=True)
    zip = models.CharField(max_length=6, blank=True)
    
    photo = models.ImageField(upload_to="images/userBioPics/%Y/%m/%d", blank=True)
    #This is a new line
