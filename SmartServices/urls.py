from typing import Pattern
from django.contrib import admin
from django.urls import path
from . import views

app_name = "SmartServices"


urlpatterns = [
    path('',views.home,name= "home"),
    path('base/',views.partnerhome,name= "base"),
    path('About/',views.Aboutus,name= "about"),
    path('Contact/',views.Contact,name= "contact"),
 
    path('Email/',views.SuccesEmail,name= "email"),
    path('register/', views.register, name="register"),
    path('login/',views.loginpage, name= "login"),
    path('logout/',views.logoutUser, name= "logout"),

    path('HirePage/',views.HirePage, name= "HirePage"),

    path(r'form/',views.CreatePatner, name= "form"),
    # path(r'form/',views.FinalPlaceOrder, name= "form2"),

    path(r'worker/<slug:slug>/',views.worker_details, name= "worker_details"),

    path('search/<slug:category_slug>/', views.category_list, name= "category_list"),
]