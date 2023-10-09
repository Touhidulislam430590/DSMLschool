from django.shortcuts import redirect, render, get_object_or_404, HttpResponse
from django.urls import reverse
from .models import pytutorial

# Create your views here.

def home(request):
    posts = pytutorial.objects.all()
    return render(request, "content/python/home.html", {'posts':posts})


def content(request, slug):
    posts = pytutorial.objects.all()
    post = get_object_or_404(pytutorial, slug=slug)
    return render(request, 'content/python/content.html', {'content':post, 'posts':posts})


def contentid(request, id):
    nextid = id+1
    try:
        nextPost = pytutorial.objects.get(id=nextid)
        url = reverse("py:content", kwargs={'slug': nextPost.slug})
    except pytutorial.DoesNotExist:
        url = reverse('py:python')
        
    return redirect(url)


def contentidprev(request, id):
    previd = id-1
    try:
        prevPost = pytutorial.objects.get(id=previd)
        urling = reverse("py:content", kwargs={'slug': prevPost.slug})
    except pytutorial.DoesNotExist:
        urling = reverse('py:python')

    return redirect(urling)

    # return HttpResponse(previd)

