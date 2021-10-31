from django import urls
from django.urls import path
from . import views

app_name = 'fileshareapp'

urlpatterns = [
    path('home/', views.home, name='Home'),
    path('share/', views.share, name= 'Share'),
    path('myposts/', views.user_posts, name='Myposts'),
    path('myposts/delete/<str:pk>',views.delete, name='delete'),
]
