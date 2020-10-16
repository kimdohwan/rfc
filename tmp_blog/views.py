from django.shortcuts import render

from tmp_blog.models import Post


def index(request):
    return render(request, 'tmp_blog/index.html', {})


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'tmp_blog/post_list.html', {'posts': posts})
