from main.models import Post


def search(request):
    posts = Post.objects.all()
    context = {}
    if "search" in request.GET:
        query = request.GET.get("q")
        search_box = request.GET.get("search-box")
        if search_box == "content":
            objects = posts.filter(content__icontains=query)
        else:
            objects = posts.filter(title__icontains=query)
        context.update({
            "objects": objects,
            "query": query
        })
    return context
