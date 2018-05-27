from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView, TemplateView

from tribes.models import Tribe


class IndexView(ListView):
    template_name = 'tribes/index.html'
    context_object_name = 'all_tribes'

    def get_queryset(self):
        return Tribe.objects.all()

class DetailView(DetailView):
    model = Tribe
    template_name = 'tribes/info.html'
    
def delete_tribe(request, tribe_id):
    tribe = Tribe.objects.get(pk=tribe_id)
    tribe.delete()
    all_tribes = Tribe.objects.all()
    return render(request, 'tribes/index.html', {'all_tribes': all_tribes})

############################### NOT CURRENTLY USING ###############################

class TemplateIndexView(TemplateView):
    template_name = 'tribes/index.html'
    
    def get(self, request):
        all_tribes = Tribe.objects.all()
        args = {'all_tribes':all_tribes}
        return render(request, self.template_name, args)

def view_info_with_pk(request, pk=None):
    tribe = get_object_or_404(Tribe, pk=pk)
    args = {'tribe': tribe}
    return render(request, 'tribes/info.html', args)