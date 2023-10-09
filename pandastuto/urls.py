from django.urls import path
from . import views

app_name = 'pandas'

urlpatterns = [
    path('', views.home, name='pandas'),
    path('content/<slug:slug>/', views.content, name='pandascontent'),
]