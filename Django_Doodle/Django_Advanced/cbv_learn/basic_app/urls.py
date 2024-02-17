from django.urls import path
from basic_app import views
# from django.conf.urls import url

app_name = 'basic_app'

urlpatterns = [
    path('', views.SchoolListView.as_view(), name='SclList'),
    path('<int:pk>/', views.SchoolDetailView.as_view(), name='SclDetail'),
    path('create/', views.SchoolCreateView.as_view(), name='SclCreate'),
    path('update/<int:pk>/', views.SchoolUpdateView.as_view(), name='SclUpdate'),
    path('delete/<int:pk>/', views.SchoolDeleteView.as_view(), name='SclDelete'),
]