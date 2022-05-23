from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'home.html')


def about(request):
    x = "Rahaf Adel Alrowithi"
    return render(request, 'about.html',{"x":x})
