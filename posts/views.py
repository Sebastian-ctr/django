from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def post_home(request):
    context = {
        "tittle": "List"
    }
    return render(request, 'home.html', context)