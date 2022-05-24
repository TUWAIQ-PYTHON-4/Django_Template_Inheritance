# Create your views here.
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "home.html")


def about(request):
    fname = 'Emtinan'
    lname = 'Alharbi'
    return render(request, "about.html", {'fname': fname, 'lname': lname})
