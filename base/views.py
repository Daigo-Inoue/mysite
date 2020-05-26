#from django.shortcuts import render
#from django.http import HttpResponse
#from django.template import loader

'''
def top(request):
    #template = loader.get_template('base/top.html')
    ctx = {'title': 'Django学習ちゃんねる(仮)'}
    #return HttpResponse(template.render(ctx, request))
    return render(request, 'base/top.html', ctx)
'''
from builtins import super

from django.views.generic import TemplateView

class TopView(TemplateView):
    template_name = 'base/top.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = 'IT学習ちゃんねる(仮)'
        return ctx