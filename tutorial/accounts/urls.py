from django.urls import include, path
from django.contrib.auth.views import login
from . import views

urlpatterns = [
    path('', views.home),
    path('login/', login, {'template_name':'accounts/login.html'})
]
