from django.urls import path
from . import views


app_name = 'matplot'

urlpatterns = [
    path('', views.home, name='matplot'),
    path('content/<slug:slug>/', views.content, name='matplotcontent'),
]