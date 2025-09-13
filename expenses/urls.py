"""
URL configuration for exptracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import hello_world  , home,addexpense,add_money, login_view, logout_view,register_view, expense_log, edit_expense, delete_expense
from . import views 
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    path('',home, name='home'),  # Home view
    path('add-expense/', addexpense, name='add_expense'),
    path('add-money/', views.add_money, name='add_money'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register_view, name='register'),    
    path('expense-log/', views.expense_log, name='expense_log'),
    path('edit-expense/<int:expense_id>/', views.edit_expense, name='edit_expense'),
    path('delete-expense/<int:expense_id>/', views.delete_expense, name='delete_expense'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),

]
