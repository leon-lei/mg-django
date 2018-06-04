from django.contrib import admin
from tribes.models import Event, Org, Tribe

class EventAdmin(admin.ModelAdmin):
    list_display = ('event_date', 'event_name', 'location', 'tribe')

    def get_queryset(self, request):
        queryset = super(EventAdmin, self).get_queryset(request)
        queryset = queryset.order_by('-event_date', 'event_name')
        return queryset

class OrgAdmin(admin.ModelAdmin):
    list_display = ('name',)

    def get_queryset(self, request):
        queryset = super(OrgAdmin, self).get_queryset(request)
        queryset = queryset.order_by('-name')
        return queryset

class TribeAdmin(admin.ModelAdmin):
    list_display = ('tribe_name', 'chieftain', 'created')

    def get_queryset(self, request):
        queryset = super(TribeAdmin, self).get_queryset(request)
        queryset = queryset.order_by('-tribe_name', 'chieftain')
        return queryset

admin.site.register(Event, EventAdmin)
admin.site.register(Tribe, TribeAdmin)
admin.site.register(Org, OrgAdmin)
