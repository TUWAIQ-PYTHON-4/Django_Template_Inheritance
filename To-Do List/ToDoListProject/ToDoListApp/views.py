from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"home.html")
def about(request):
    return render(request,"about.html")
def base(request):
    return render(request,"base.html")

def about(request):
    context = {'f_name': 'Faisal', 'l_name': 'alsneed'}
    return render(request, 'about.html', context)


def home(request):
    return render(request, 'home.html', {})