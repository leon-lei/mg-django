from django.urls import path
from tribes.views import IndexView
from . import views

app_name='tribes'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('info/<int:pk>/', views.view_info, name='view_info'),
]
