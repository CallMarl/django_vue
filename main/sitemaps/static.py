from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

class SinglePage(Sitemap) :

    changefreq = "monthly"

    priority = 1

    def items(self) :
        return [
            'home_page'
        ]

    def location(self, item) :
        if item :
            return reverse(item)
