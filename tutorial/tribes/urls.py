from django.urls import path
from tribes.views import IndexView
from . import views

app_name='tribes'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('info/', IndexView.as_view(), name='view_info'),
    path('info/<int:pk>/', views.view_info_with_pk, name='view_info_with_pk'),
]
