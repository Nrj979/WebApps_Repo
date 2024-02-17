from basic_app import views
from django.urls import path

app_name = 'basic_app'

urlpatterns = [
    path('other/', views.other, name='other'),
    path('relative_url/', views.relative_url, name='relative_url'),
]