from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Post

# Create your views here.

def post_home(request):
    queryset = Post.objects.all()
    context = {
        "object_list": queryset,
        "tittle": "List"
    }
    return render(request, 'home.html', context)

def post_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    context = {
        "tittle": instance.tittle,
        "instance": instance
    }
    return render(request, 'post_detail.html', context)
