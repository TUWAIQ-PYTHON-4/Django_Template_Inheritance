from django.shortcuts import render
from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, "base.html")


def home(request):
    return render(request, "home.html")


def about(request):
    name = "Ali Mushbari"
    return render(request, "about.html", {"name": name})
