from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def about(request):
    context = {'f_name': 'Abdulhad', 'l_name': 'Ahmed'}
    return render(request, "about.html", context)
