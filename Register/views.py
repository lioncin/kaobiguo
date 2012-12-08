from django.shortcuts import render_to_response
from kaobiguo.KBGUser.forms import ReginsterForm
from kaobiguo.utils.templates import get_context

def register(request):
    context = get_context(request)
    if request.method == 'GET':
        form = ReginsterForm(request.GET)
        context['form'] = form
        return render_to_response('register.html', context)
    else:
        pass
