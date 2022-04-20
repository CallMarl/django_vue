from django.shortcuts import render

# Create your views here.
def view_vuejs(request) :
    return render(request, 'pages/vuejs.html')
