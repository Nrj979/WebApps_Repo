from appTwo import views
from django.urls import path

app_name = 'appTwo'

urlpatterns = [
    path('', views.index, name='index'),
    path('help/', views.help, name='help'),
    path('users/', views.users, name='users'),
]