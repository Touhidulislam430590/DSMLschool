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


def disclaimer(request):
    return render(request, 'home/disclaimer.html')


def privacy_policy(request):
    return render(request, 'home/privacy_policy.html')


def terms_and_condition(request):
    return render(request, 'home/terms_and_conditions.html')