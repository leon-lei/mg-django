from django.contrib import admin
from home.models import Friend, Post

class FriendAdmin(admin.ModelAdmin):
    list_display = ('current_user',)

    def get_queryset(self, request):
        queryset = super(FriendAdmin, self).get_queryset(request)
        queryset = queryset.order_by('-current_user')
        return queryset

class PostAdmin(admin.ModelAdmin):
    list_display = ('created', 'user', 'post')

    def get_queryset(self, request):
        queryset = super(PostAdmin, self).get_queryset(request)
        queryset = queryset.order_by('-created', 'user')
        return queryset


admin.site.register(Friend, FriendAdmin)
admin.site.register(Post, PostAdmin)

