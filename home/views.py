from django.shortcuts import render
from .models import ContactModel

# Create your views here.

def homepage(request):
    return render(request, 'home/homepage.html')


def contact(request):
    if request.method == 'POST':
        email = request.POST['email']
        message = request.POST['message']

        ContactModel.objects.create(email = email, message = message)

    return render(request, 'home/contact.html')


def about(request):
    return render(request, 'home/about.html')