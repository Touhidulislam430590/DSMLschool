from django.urls import path
from . import views


app_name = 'py'

urlpatterns = [
    path('', views.home),
    path('content/<int:pk>/', views.content, name='content'),
]