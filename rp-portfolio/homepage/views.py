from homepage.models import Home
from django.shortcuts import render

def index_view(request):
    home = Home.objects.get()
    context = {
        'home': home
    }
    return render(request, 'index.html', context)