from django.shortcuts import render


# Create your views here.
from django.template import context


#def base(request):
    #return render(request, "base.html")


def about(request):
    context = {'f_name': 'Abdulaziz', 'l_name': 'Altariqi'}
    return render(request, 'about.html', context)


def home(request):
    return render(request, 'home.html', {})
