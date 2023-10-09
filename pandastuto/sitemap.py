from django.contrib.sitemaps import Sitemap
from .models import pandastutorial


class PandasSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return pandastutorial.objects.all().order_by('id')