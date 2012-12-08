from django.template.context import RequestContext
from django.conf import settings

def get_context(request, activeApp=None):
    context = RequestContext(request)
    context['debug'] = settings.DEBUG
    context['DEBUG'] = settings.DEBUG
    context['MEDIA_URL'] = settings.MEDIA_URL
    return context
