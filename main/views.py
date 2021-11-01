from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Page, Paginator, PageNotAnInteger, EmptyPage
from .models import Author, Category, Post, Comment, Reply
from .utils import update_views
from .forms import PostForm

# Create your views here.


def home(request):
    boards = Category.objects.all()
    context = {
        "boards": boards,
        "title": "Crashboard"
    }
    return render(request, "home.html", context)


def board(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(approved=True, categories=category)
    paginator = Paginator(posts, 3)
    page = request.GET.get("page")
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts.paginator.page(paginator.num_pages)
    context = {
        "posts": posts,
        "category": category,
        "title": "Posts"
    }
    return render(request, "board.html", context)


def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    author = Author.objects.get(user=request.user)
    post.approved = True
    if "comment-form" in request.POST:
        comment = request.POST.get("comment")
        new_comment, created = Comment.objects.get_or_create(
            user=author, content=comment)
        post.comments.add(new_comment.id)

    if "reply-form" in request.POST:
        reply = request.POST.get("reply")
        comment_id = request.POST.get("comment_id")
        comment_obj = Comment.objects.get(id=comment_id)
        new_reply, created = Reply.objects.get_or_create(
            user=author, content=reply)
        comment_obj.replies.add(new_reply.id)

    context = {
        "post": post,
        "title": post.title
    }
    update_views(request, post)
    return render(request, "post.html", context)


@login_required
def create_post(request):
    context = {}
    form = PostForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        author = Author.objects.get(user=request.user)
        new_post = form.save(commit=False)
        new_post.user = author
        new_post.save()
        return redirect("home")
    context.update({
        "form": form,
        "title": "Create New Post"
    })
    return render(request, "create_post.html", context)


def search_result(request):

    return render(request, "search_result.html")
