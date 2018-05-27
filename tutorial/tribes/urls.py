from django.urls import path
from tribes.views import TribeCreateView, TribeDetailView, IndexView
from . import views

app_name='tribes'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', TribeDetailView.as_view(), name='tribe-details'),
    path('tribe/create/', TribeCreateView.as_view(), name='tribe-create'),
    path('tribe/delete/<int:tribe_id>/', views.delete_tribe, name='tribe-delete'),
]
