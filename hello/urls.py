from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.jam, name="jam"),
    path("leyla", views.leyla, name="leyla")
]