from django.shortcuts import render, get_object_or_404
from .models import matplottutorial

# Create your views here.

def home(request):
    posts = matplottutorial.objects.all()
    return render(request, "content/matplot/matplothome.html", {'posts':posts})

def content(request, slug):
    posts = matplottutorial.objects.all()
    post = get_object_or_404(matplottutorial, slug=slug)
    return render(request, 'content/matplot/matplotcontent.html', {'content':post, 'posts':posts})

