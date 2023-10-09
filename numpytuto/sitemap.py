from django.contrib.sitemaps import Sitemap
from .models import numpytutorial


class NumpySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return numpytutorial.objects.all().order_by('id')