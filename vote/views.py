from django.shortcuts import render,redirect
# from . models import 

def index(request):
    return render(request,"index.html")

def home(request):
    return render(request,"home.html")

def voter_reg(request):
    return render(request,"voter_reg.html")

def voter_login(request):
    return render(request,"voter_login.html")

def officer_reg(request):
    return render(request,"officer_reg.html")

def officer_login(request):
    return render(request,"officer_login.html")

