from django.shortcuts import render

# Create your views here.
def base(request):
    base = request.GET.get("base")
    return render(request,"base.html")

def home (request):
    home = request.GET.get("home")
    return render(request,'home.html',{"home": home})
def about (request):
    about = request.GET.get("about")
    return render(request,'about.html',{"about": about})

