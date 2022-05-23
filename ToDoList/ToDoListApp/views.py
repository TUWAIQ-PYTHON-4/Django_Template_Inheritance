from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


# def base(request):
#    return render(request, 'base.html')

def home(request):
    return render(request, 'home.html')


def about(request):
    firstName = 'Asma'
    lastName = 'Abufayah'

    return render(request, 'about.html', {'firstName': firstName, 'lastName': lastName})
