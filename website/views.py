from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse(request, 'website/home.html')

def pictures(request):
    return HttpResponse(request, 'website/pictures.html')

def post(request):
    return HttpResponse(request, 'website/post.html')

def findme(request):
    return HttpResponse(request, 'website/findme.html')

def navbar(request):
    return HttpResponse(request, 'website/navbar.html')

def main(request):
    return HttpResponse(request, 'website/main.html')