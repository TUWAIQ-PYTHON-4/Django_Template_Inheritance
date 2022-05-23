from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    #context_dictionary
    fname = request.GET.get('fname') or 'jan'
    lname = request.GET.get('lname') or 'doe'
    return render(request, 'about.html', {'fname': fname, 'lname':lname})
