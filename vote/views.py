from django.shortcuts import render,redirect
# from . models import 

def index(request):
    return render(request,"index.html")

def home(request):
    return render(request,"home.html")
    
def login_officer(request):
    return render(request,"officer_login.html")

def register_officer(request):
    return render(request,"officer_registration.html")

