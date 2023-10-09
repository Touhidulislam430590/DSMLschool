from django.contrib.sitemaps import Sitemap
from .models import matplottutorial


class MatplotSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return matplottutorial.objects.all().order_by('id')