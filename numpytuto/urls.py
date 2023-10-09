from django.urls import path
from . import views


app_name = 'numpy'

urlpatterns = [
    path('', views.home, name='numpy'),
    path('content/<slug:slug>/', views.content, name='numpycontent'),
]