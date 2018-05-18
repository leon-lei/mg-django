from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from tribes.models import Tribe


class IndexView(TemplateView):
    template_name = 'tribes/index.html'
    
    def get(self, request):
        all_tribes = Tribe.objects.all()
        args = {'all_tribes':all_tribes}
        return render(request, self.template_name, args)

def view_info(request, pk=None):
    if pk:
        tribe = Tribe.objects.get(pk=pk)
    else:
        return HttpResponse('You need a tribe id')
    args = {'tribe': tribe}
    return render(request, 'tribes/info.html', args)