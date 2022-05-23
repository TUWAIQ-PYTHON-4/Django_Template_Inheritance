from django.shortcuts import render

# Create your views here.
from django.template import context


def home(request):
    return render(request, 'home.html')


def about(request):
    first_name = 'Wafa'
    last_name = 'Ali'
    return render(request, 'about.html', {'first_name': first_name, 'last_name': last_name})

