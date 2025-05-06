# accounts/urls.py
from django.urls import path
from .import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.register_user, name='Register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]
