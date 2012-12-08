from django.contrib import admin
from kaobiguo.Message.models import Message, MessageBody,MessageCC

admin.site.register(Message)
admin.site.register(MessageBody)
admin.site.register(MessageCC)