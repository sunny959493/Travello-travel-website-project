from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home),
    path('about', views.about),
    path('destination', views.travel_destination)
]