from django.shortcuts import render


def home(request):
    
    return render(request,'info/home.html')

def uslugi(request):
    return render(request,'info/uslugi.html')