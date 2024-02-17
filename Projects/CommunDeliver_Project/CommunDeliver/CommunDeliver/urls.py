"""
URL configuration for CommunDeliver project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from deliver.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',login_page),
    path('admin_page/',admin_page,name='admin_page'),
    path('verify_partner/',verify_partner,name='verify_partner'),
    path("login_page/",login_page,name="login_page"),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    path('customer_register_page/',customer_register_page,name='customer_register_page'),
    path('register_customer/',register_customer,name='register_customer'),
    path('partner_register_page/',partner_register_page,name='partner_register_page'),
    path('register_partner/',register_partner,name='register_partner'),
    path('home_page/',home_page,name='home_page'),
    path('partner_home_page/',partner_home_page,name='partner_home_page'),
    path('add_request/',add_request,name='add_request'),
    path('send_requests/',send_requests,name='send_requests'),
    path('post_avail/',post_avail,name='post_avail'),
    path('add_availability/',add_availability,name='add_availability'),
    path('delivery_request/',delivery_request,name='delivery_request'),
    path('view_request/',view_request,name='view_request'),
    path('respond_request/',respond_request,name='respond_request'),
    path('update_status/',update_status,name='update_status'),
    path('change_status/',change_status,name='change_status'),
    path('partner_status/',partner_status,name='partner_status'),
    path('payment_page/',payment_page,name='payment_page'),
    path('pay/',pay,name='pay'),
    path('feedback_page/',feedback_page,name='feedback_page'),
    path('add_feedback/',add_feedback,name='add_feedback'),
    
    
]



# from django.shortcuts import render, redirect
# from .models import Partner

# def login_view(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         # Check if it's the admin
#         if email == 'admin@mail.in' and password == 'Admin@123':
#             get_partners = Partner.objects.all()
#             print(get_partners)
#             return render(request, 'admin_home.html', {'partners': get_partners})
#         else:
#             # Try to filter the Partner based on email and password
#             matching_partners = Partner.objects.filter(partnermail=email, partnerpassword=password)

#             if matching_partners.exists():
#                 partner = matching_partners.first()

#                 # Assuming you have a boolean field 'is_partner' in your Partner model
#                 if partner.is_partner:
#                     return render(request, 'partner_home.html')
#                 else:
#                     return render(request, 'customer_home.html')
#             else:
#                 # No matching partner found
#                 return render(request, 'login.html', {'error_message': 'Invalid login credentials'})

#     return render(request, 'login.html')

