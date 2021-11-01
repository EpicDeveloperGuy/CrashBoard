from django.urls import path
from .views import home, board, post, create_post, search_result

urlpatterns = [
    path("", home, name="home"),
    path("board/<slug>/", board, name="board"),
    path("post/<slug>/", post, name="post"),
    path("create_post", create_post, name="create_post"),
    path("search_reuslt", search_result, name="search_result")
]
