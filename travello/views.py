from django.shortcuts import render
from django.http import HttpResponse
from .models import destination, t_destination

def home(request):
    dests = destination.objects.all()
    return render(request, 'index.html', {'dests': dests})

def about(request):
    return render(request, 'about.html')

def travel_destination(request):
    t_dests = t_destination.objects.all()
    return render(request, 'travel_destination.html', {'t_dests': t_dests})
