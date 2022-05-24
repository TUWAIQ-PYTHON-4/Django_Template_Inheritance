from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})

def about(request):
    context = {'f_name': 'Mohannd', 'l_name': 'Saeed'}
    return render(request, 'about.html', context)
