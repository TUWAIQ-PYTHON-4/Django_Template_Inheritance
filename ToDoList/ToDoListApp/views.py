from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def about(request):
    first_name="Hawra"
    last_name="Alomani"
    return render(request, "about.html", {"first_name":first_name,"last_name":last_name})
