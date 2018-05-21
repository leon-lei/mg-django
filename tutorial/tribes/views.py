from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views.generic import TemplateView

from tribes.models import Tribe


class IndexView(TemplateView):
    template_name = 'tribes/index.html'
    
    def get(self, request):
        all_tribes = Tribe.objects.all()
        args = {'all_tribes':all_tribes}
        return render(request, self.template_name, args)

def view_info(request, pk):
    try:
        tribe = Tribe.objects.get(pk=pk)
    except Tribe.DoesNotExist:
        raise Http404('Tribe does not exist')
    args = {'tribe': tribe}
    return render(request, 'tribes/info.html', args)