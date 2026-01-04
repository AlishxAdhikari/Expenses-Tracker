
from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import hello_world  , home,addexpense,add_money, login_view, logout_view,register_view, expense_log, edit_expense, delete_expense
from . import views 
from django.contrib.auth import views as auth_views
from .views import about
print("🔥 LOADING expenses.urls 🔥")



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
    path('about/',views.about,name='about'),
    
    

]
