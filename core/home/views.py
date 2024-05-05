from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    people =[
        {"name":"Shubham","age":28},
        {"name":"Rohan","age":28},
        {"name":"Vicky Kaushal","age":23},
        {"name":"Sandeep","age":21},
        {"name":"Randeep","age":26}
        
    ]
    return render(request,r'home/templates/index.html',context={'people':people})

def success_page(request):
    return HttpResponse("<h1>This is a success page.</h1>")

def templates(request):
    return render(request,"index.html")
