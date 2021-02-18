from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def leyla(request, name):
    return HttpResponse(f"you suck, {name.capitalize()}!")

def jam(request, name):
    return render(request, "hello/jam.html", {
        "name": name.capitalize()
    })