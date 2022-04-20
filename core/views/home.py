from django.shortcuts import render
from django.views import View

class Home(View) :

    template_name   = 'pages/home.html'

    def get(self, request, *args, **kwargs) :
        return render(request, self.template_name, context = {})
