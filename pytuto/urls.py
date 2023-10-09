from django.urls import path
from . import views


app_name = 'py'


urlpatterns = [
    path('', views.home, name='python'),
    path('content/<slug:slug>/', views.content, name='content'),
    path('next/<int:id>/', views.contentid, name='contentId'),
    path('prev/<int:id>/', views.contentidprev, name='contentIdprev')
]

