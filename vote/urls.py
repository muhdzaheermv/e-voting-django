"""
URL configuration for votesphere project.

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
from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    
    #voter
    path('voter_login/',views.voter_login,name='voter_login'),
    path('voter_reg/',views.voter_reg,name='voter_reg'),
    
    #officer
    path('officer_login/',views.officer_login,name='officer_login'),
    path('officer_reg/',views.officer_reg,name='officer_reg'),
    path('officer_home/',views.officer_home,name='officer_home'),
    path('officer_profile/',views.officer_profile,name='officer_profile'),
    
    
]
