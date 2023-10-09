from django.urls import path
from . import views




urlpatterns = [
    path('', views.homepage, name='home'),
    path('home/', views.homepage, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    
    path('disclaimer/', views.disclaimer, name='disclaimer'),
    path('privacy_policy/', views.privacy_policy, name='policy'),
    path('terms_and_conditions/', views.terms_and_condition, name='conditions'),
]