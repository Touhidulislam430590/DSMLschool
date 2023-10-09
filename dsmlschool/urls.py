"""dsmlschool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.contrib.sitemaps.views import sitemap
from pytuto.sitemap import PytutoSitemap
from numpytuto.sitemap import NumpySitemap
from pandastuto.sitemap import PandasSitemap
from matplotlibtuto.sitemap import MatplotSitemap


# Django Admin Panel Customization
admin.site.site_header = 'DSMLschool Admin'
admin.site.site_title = 'Admin Panel'
admin.site.index_title = 'Data Science Machine Learning School Administration Panel'

sitemaps = {
    'python' : PytutoSitemap,
    'numpy' : NumpySitemap,
    'pandas' : PandasSitemap,
    'matplot' : MatplotSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('python/', include('pytuto.urls')),
    path('numpy/', include('numpytuto.urls')),
    path('pandas/', include('pandastuto.urls')),
    path('matplot/', include('matplotlibtuto.urls')),

    path('sitemap.xml', sitemap, {'sitemaps':sitemaps}),
]

handler404 = 'home.views.error_404'
