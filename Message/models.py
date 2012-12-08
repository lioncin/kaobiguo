from django.db import models
from django.contrib.auth.models import User

PROVINCE_CHOICES = ()

MESSAGE_STATUS = ()

class Message(models.Model):
    sender = models.ForeignKey(User, null=True)
    created_time = models.DateTimeField(auto_now_add=True)

class MessageBody(models.Model):
    message = models.ForeignKey(Message)
    course = models.CharField(max_length=255)
    time = models.DateTimeField()
    province = models.CharField(max_length=2, choices=PROVINCE_CHOICES)
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    from_time = models.CharField(max_length=255)
    to_time = models.CharField(max_length=255)
    price = models.IntegerField()

class MessageStatus(models.Model):
    message = models.ForeignKey(Message)
    stats = models.CharField(max_length=2, choices=MESSAGE_STATUS)
    
class MessageCC(models.Model):
    message = models.ForeignKey(Message)
    user = models.ForeignKey(User)
    
