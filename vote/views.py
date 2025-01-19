from django.shortcuts import render,redirect
from . models import ElectionOfficer

def index(request):
    return render(request,"index.html")

def home(request):
    return render(request,"home.html")

def voter_reg(request):
    return render(request,"voter_reg.html")

def voter_login(request):
    return render(request,"voter_login.html")

def officer_reg(request):
   if request.method =='POST':
      regno = request.POST.get('regno')
      name = request.POST.get('rname')
      uname = request.POST.get('runame')
      email = request.POST.get('remail')
      phone = request.POST.get('rcontact')
      address=request.POST.get('raddress')
      passw = request.POST.get('rpass')
      ElectionOfficer(register_no=regno,name=name,phone_number=phone,email=email,username=uname,address=address,password=passw).save()
      return render(request,'officer_login.html')
   else:
      return render(request,"officer_reg.html")
    

def officer_login(request):
    if request.method=='POST':
        regno =  request.POST.get('regno')
        uname = request.POST.get('runame')
        passw = request.POST.get('rpass')
        cr = ElectionOfficer.objects.filter(register_no=regno,username=uname,password=passw)
        if cr:
            details = ElectionOfficer.objects.get(username=uname, password = passw,register_no=regno)
            username = details.username
            request.session['cs']=username
            regno = details.register_no
            request.session['regno']=regno
            
            return render(request,'officer_home.html')
        else:
            message="Invalid Username Or Password"
            return render(request,'officer_login.html',{'me':message})
    else: 
        return render(request,'officer_login.html')
    
def officer_home(request):
    return render(request,"officer_home.html")
    
def officer_profile(request):
    c=request.session['cs']
    cr=ElectionOfficer.objects.get(username=c)
    pregno=cr.register_no
    pname=cr.name
    puname=cr.username
    pemail=cr.email
    pcontact=cr.phone_number
    paddress=cr.address
    pcreatedat=cr.created_at
    return render(request,"officer_profile.html",{'regno':pregno,'name':pname,'uname':puname,'contact':pcontact,'email':pemail,'address':paddress,'created_at':pcreatedat})

