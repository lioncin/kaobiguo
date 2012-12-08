from django.http import HttpResponse
import json
from kaobiguo.Message.models import Message


def getCurrentHotMsgs(request):
    msgs = Message.objects.all()
    if msgs:
        return HttpResponse(json.dumps(msgs))
    else:
        return HttpResponse(json.dumps('err'))