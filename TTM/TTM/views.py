from django.shortcuts import render


def homePage(request):
    return render(request,"index.html")
def LoginPage(request):
    return render(request,"login.html")
def ContactPage(request):
    return render(request,"Contact.html")
def AboutPage(request):
    return render(request,"About.html")