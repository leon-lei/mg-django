from django.contrib import admin
from django.urls import include, path
from tutorial import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login_redirect, name='login_redirect'),
    path('admin/', admin.site.urls),
    path('account/', include('accounts.urls', namespace='accounts')),
    path('home/', include('home.urls', namespace='home')),
    path('tribes/', include('tribes.urls', namespace='tribes')),
] 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
