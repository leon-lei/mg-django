from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from tribes.models import Tribe, Org

class TribeCreate(CreateView):
    model = Tribe
    fields = ['tribe_name', 'chieftain', 'image']

class TribeDelete(DeleteView):
    model = Tribe
    success_url = reverse_lazy('tribes:index')

class TribeDetail(DetailView):
    model = Tribe
    template_name = 'tribes/info.html'

class TribeUpdate(UpdateView):
    model = Tribe
    fields = ['tribe_name', 'chieftain', 'image']

class IndexView(ListView):
    template_name = 'tribes/index.html'
    context_object_name = 'all_tribes'
    
    def get_queryset(self):
        return Tribe.objects.all()

class OrgCreate(CreateView):
    model = Org
    fields = ['name', 'captain', 'members', 'image']

class OrgDetail(DetailView):
    model = Org
    template_name = 'tribes/orginfo.html'

############################### NOT CURRENTLY USING ###############################

class TemplateIndexView(TemplateView):
    template_name = 'tribes/index.html'
    
    def get(self, request):
        all_tribes = Tribe.objects.all()
        args = {'all_tribes':all_tribes}
        return render(request, self.template_name, args)

def delete_tribe(request, tribe_id):
    tribe = Tribe.objects.get(pk=tribe_id)
    tribe.delete()
    all_tribes = Tribe.objects.all()
    return render(request, 'tribes/index.html', {'all_tribes': all_tribes})

def view_info_with_pk(request, pk=None):
    tribe = get_object_or_404(Tribe, pk=pk)
    args = {'tribe': tribe}
    return render(request, 'tribes/info.html', args)