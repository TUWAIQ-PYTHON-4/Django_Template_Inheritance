from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    name = 'Nourah Alsaadan'
    return render(request,'about.html', {'name':name})

