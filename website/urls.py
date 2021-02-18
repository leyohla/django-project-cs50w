from django.urls import path
from . import views

# app_name = "photos"
urlpatterns = [
    path("", views.main, name="main"),
    path("home", views.home, name="home"),
    path("navbar", views.navbar, name="navbar"),
    path("pictures", views.pictures, name="pictures"),
    path("post", views.post, name="post"),
    path("findme", views.findme, name="findme")
    
]