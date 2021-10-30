from django.shortcuts import render, get_object_or_404
from .models import Author, Category, Post
from .utils import update_views

# Create your views here.


def home(request):
    boards = Category.objects.all()
    context = {
        "boards": boards
    }
    return render(request, "home.html", context)


def board(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(approved=True, categories=category)
    context = {
        "posts": posts
    }
    return render(request, "board.html", context)


def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {
        "post": post
    }
    update_views(request, post)
    return render(request, "post.html", context)
