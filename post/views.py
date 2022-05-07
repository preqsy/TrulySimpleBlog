from django.shortcuts import render, get_object_or_404
from .models import Post


def index(request):
    posts = Post.objects.filter(featured=True)
    return render(request, 'index.html', {'posts': posts})


def post(request, pk):
    posts = Post.objects.get(id=pk)
    return render(request, 'post.html', {'posts': posts})
