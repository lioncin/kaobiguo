from django.shortcuts import render_to_response
from kaobiguo.utils.templates import get_context

def main(request):
    context = get_context(request)
    return render_to_response('home.html', context)
