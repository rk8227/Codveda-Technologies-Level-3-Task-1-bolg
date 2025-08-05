from django.shortcuts import render
from .models import Post

def blog_list(request):
    posts = Post.objects.all()
    return render(request, 'blog_list.html', {'posts': posts})

