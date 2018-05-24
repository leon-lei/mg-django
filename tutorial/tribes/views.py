from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

from tribes.models import Tribe


class IndexView(TemplateView):
    template_name = 'tribes/index.html'
    
    def get(self, request):
        all_tribes = Tribe.objects.all()
        args = {'all_tribes':all_tribes}
        return render(request, self.template_name, args)

def view_info_with_pk(request, pk=None):
    tribe = get_object_or_404(Tribe, pk=pk)
    args = {'tribe': tribe}
    return render(request, 'tribes/info.html', args)