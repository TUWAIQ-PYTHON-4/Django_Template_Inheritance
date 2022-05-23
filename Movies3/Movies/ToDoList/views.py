from django.shortcuts import render
from django.contrib import auth

from django.shortcuts import render


def base(request):

    return render(request, "base.html")


def home_view(request):

    return render(request, "home.html")


def about_view(request):
    return render(request, "about.html")
