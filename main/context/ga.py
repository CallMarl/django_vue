from django.conf import settings

def ga(request):
    return {
        'GA_KEY': settings.GOOGLE_ANALYTICS_KEY,
    }
