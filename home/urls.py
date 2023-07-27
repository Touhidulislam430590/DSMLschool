from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),
    path('home/', views.homepage),
    path('contact/', views.contact),
    path('about/', views.about),
]