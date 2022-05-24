from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def about(request):
    name = {'f_name': 'lama', 'l_name': 'Alkhalifah'}
    return render(request, 'about.html', name)
