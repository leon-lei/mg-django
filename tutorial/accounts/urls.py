from django.urls import include, path
from django.contrib.auth.views import (
	login, logout, password_reset, password_reset_done, password_reset_confirm,
	password_reset_complete
)
from . import views

urlpatterns = [
    path('', views.home),
    path('login/', login, {'template_name':'accounts/login.html'}),
    path('logout/', logout, {'template_name':'accounts/logout.html'}),
    path('register/', views.register, name='register'),
    path('profile/', views.view_profile, name='view_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('change-password/', views.change_password, name='change_password'),
    path('reset-password/', password_reset, name='reset_password'),
    path('reset-password/done/', password_reset_done, name='password_reset_done'),
    path('reset-password/confirm/<uidb64>/<token>/', password_reset_confirm, name='password_reset_confirm'),
    path('reset-password/complete/', password_reset_complete, name='password_reset_complete'),
]
