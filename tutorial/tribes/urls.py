from django.urls import path
from tribes.views import DetailView, IndexView
from . import views

app_name='tribes'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', DetailView.as_view(), name='tribe_details'),
    path('delete_tribe/<int:tribe_id>/', views.delete_tribe, name='delete_tribe')
]
