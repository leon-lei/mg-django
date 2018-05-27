from django.urls import path
from tribes.views import DetailView, IndexView
from . import views

app_name='tribes'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('info/', IndexView.as_view(), name='view_info'),
    path('info/<int:pk>/', DetailView.as_view(), name='view_info_with_pk'),
    path('delete_tribe/<int:tribe_id>/', views.delete_tribe, name='delete_tribe')
]
