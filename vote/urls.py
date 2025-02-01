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
    
    #election
    # path('election_reg/',views.election_reg,name='election_reg'),
    # path('election_list/',views.election_list,name='election_list'),,,,
    
    path('list/', views.polls_list, name='list'),
    path('list/user/', views.list_by_user, name='list_by_user'),
    path('add/', views.polls_add, name='add'),
    path('edit/<int:poll_id>/', views.polls_edit, name='edit'),
    path('delete/<int:poll_id>/', views.polls_delete, name='delete_poll'),
    path('end/<int:poll_id>/', views.end_poll, name='end_poll'),
    path('edit/<int:poll_id>/choice/add/', views.add_choice, name='add_choice'),
    path('edit/choice/<int:choice_id>/', views.choice_edit, name='choice_edit'),
    path('delete/choice/<int:choice_id>/',
         views.choice_delete, name='choice_delete'),
    path('<int:poll_id>/', views.poll_detail, name='detail'),
    path('<int:poll_id>/vote/', views.poll_vote, name='vote'),
    
    
    
]
