from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),
    path('home/', views.homepage),
    path('contact/', views.contact),
    path('about/', views.about),
    path('disclaimer/', views.disclaimer),
    path('privacy_policy/', views.privacy_policy),
    path('terms_and_conditions/', views.terms_and_condition),
]