from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {
        'title': "Homepage"
    }
    return render(request, 'store/index.html', context)