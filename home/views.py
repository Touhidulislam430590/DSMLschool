from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request, 'homepage.html')


def contact(request):
    return render(request, 'contact.html')