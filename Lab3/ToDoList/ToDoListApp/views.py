from django.shortcuts import render
def home(request):
    return render(request,"home.html")

def about(request):
    about1 = request.GET.get("about1")
    fname = 'Adnan'
    lname = 'Abo Assoud'
    return render(request,"about.html",{'fname':fname,'lname':lname})

# Create your views here.
