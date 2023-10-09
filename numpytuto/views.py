from django.shortcuts import render, get_object_or_404
from .models import numpytutorial

# Create your views here.

def home(request):
    posts = numpytutorial.objects.all()
    return render(request, "content/numpy/numpyhome.html", {'posts':posts})

def content(request, slug):
    posts = numpytutorial.objects.all()
    post = get_object_or_404(numpytutorial, slug=slug)
    return render(request, 'content/numpy/numpycontent.html', {'content':post, 'posts':posts})

