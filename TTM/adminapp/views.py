from django.http import HttpResponse
from django.shortcuts import render
from .models import Admin
def ttmhome(request):
    return render(request,"ttmhome.html")
def Loginpage(request):
    return render(request,"login.html")
def contactpage(request):
    return render(request,"contact.html")
def aboutpage(request):
    return render(request,"about.html")

# Create your views here.
def checkadminlogin(request):
    if request.method == "POST":
        adminuname = request.POST["uname"]
        adminpwd = request.POST["pwd"]
        flag = Admin.objects.filter(UserName=adminuname,password=adminpwd).value()
        if flag:
            return render(request,"ttmhome.html")
        else:
            return render(request,"loginfail.html")