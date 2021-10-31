from django import urls
from django.urls import path
from . import views

app_name = 'authentication'

urlpatterns = [
    path('', views.login_user, name='Login'),
    path('register/', views.register_user, name='Register'),
    path('logout/', views.logout_user, name='Logout'),
]
