from django.urls import path
from tribes.views import IndexView, TribeCreate, TribeDetail, TribeDelete, TribeUpdate, OrgCreate, OrgDetail, NewOrgDetail
from . import views

app_name='tribes'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', TribeDetail.as_view(), name='tribe-details'),
    path('tribe/<int:pk>/', TribeUpdate.as_view(), name='tribe-update'),
    path('tribe/<int:pk>/delete/', TribeDelete.as_view(), name='tribe-delete'),
    path('tribe/create/', TribeCreate.as_view(), name='tribe-create'),
    path('org/<int:pk>/', NewOrgDetail.as_view(), name='org-details'),
    path('org/create/', OrgCreate.as_view(), name='org-create'),
]
