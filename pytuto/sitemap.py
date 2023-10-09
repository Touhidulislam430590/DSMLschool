from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import pytutorial


class PytutoSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return pytutorial.objects.all().order_by('id')