from django.urls import include
from django.urls import path
from django.views import debug

from core.views import home

urlpatterns = [
    # Reload default django home page
    path('', debug.default_urlconf, name="home_page"),

    # Load core views with app template
    path('home',
        home.Home.as_view(
            template_name   = 'pages/home.html'
            ),
        name = 'view_home'
        )
]
