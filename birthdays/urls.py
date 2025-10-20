from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.birthday_form, name='birthday_form'),
    path('success/', views.birthday_success, name='birthday_success'),
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('create/', views.admin_create, name='admin_create'),
    path('update/<int:pk>/', views.admin_update, name='admin_update'),
    path('delete/<int:pk>/', views.admin_delete, name='admin_delete'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]