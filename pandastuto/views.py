from django.shortcuts import render, get_object_or_404
from .models import pandastutorial

# Create your views here.

def home(request):
    posts = pandastutorial.objects.all()
    return render(request, "content/pandas/pandashome.html", {'posts':posts})

def content(request, slug):
    posts = pandastutorial.objects.all()
    post = get_object_or_404(pandastutorial, slug=slug)
    return render(request, 'content/pandas/pandascontent.html', {'content':post, 'posts':posts})
