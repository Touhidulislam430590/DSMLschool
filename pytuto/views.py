from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import tutorial

# Create your views here.

def home(request):
    posts = tutorial.objects.all()
    return render(request, "content/home.html", {'posts':posts})

def content(request, pk):
    posts = tutorial.objects.all()
    post = get_object_or_404(tutorial, pk=pk)
    return render(request, 'content/content.html', {'content':post, 'posts':posts})