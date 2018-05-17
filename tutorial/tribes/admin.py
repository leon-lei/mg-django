from django.contrib import admin
from tribes.models import Event, Tribe

class EventAdmin(admin.ModelAdmin):
    list_display = ('event_date', 'event_name', 'location', 'tribe')

    def get_queryset(self, request):
        queryset = super(EventAdmin, self).get_queryset(request)
        queryset = queryset.order_by('-event_date', 'event_name')
        return queryset

class TribeAdmin(admin.ModelAdmin):
    list_display = ('tribe_name', 'chieftain', 'created')

    def get_queryset(self, request):
        queryset = super(TribeAdmin, self).get_queryset(request)
        queryset = queryset.order_by('-tribe_name', 'chieftain')
        return queryset

admin.site.register(Event, EventAdmin)
admin.site.register(Tribe, TribeAdmin)
