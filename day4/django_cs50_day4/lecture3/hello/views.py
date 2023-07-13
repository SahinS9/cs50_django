from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse('Site works perfectly')
#after creating some httpresponse go to own url file of the hello app and connect it with main app 
    return render(request, "hello/index.html")


def brian(request):
    return HttpResponse("Hello, Brian~")


def david(request):
    return HttpResponse("David!")

def greet(request, name):
    # return HttpResponse(f"Hello, {name.capitalize()}!")
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })
