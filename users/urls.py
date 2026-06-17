from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from django.urls import path
from .views import RegisterView
from . import views

from .views import (UserListView, UserDetailView, UserCreateView, UserUpdateView, UserDeleteView)

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registro/', RegisterView.as_view(), name='register'),
    path('perfil/', views.perfil_usuario, name='perfil_usuario'),
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('admin/users/', UserListView.as_view(), name='user_list'),
    path('admin/users/new/', UserCreateView.as_view(), name='admin_user_create'),
    path('admin/users/<int:pk>/', UserDetailView.as_view(), name='admin_user_detail'),
    path('admin/users/<int:pk>/edit/', UserUpdateView.as_view(), name='admin_user_update'),
    path('admin/users/<int:pk>/delete/', UserDeleteView.as_view(), name='admin_user_delete'),
]