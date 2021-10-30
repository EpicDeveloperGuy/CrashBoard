from django.urls import path
from .views import home, board, post

urlpatterns = [
    path("", home, name="home"),
    path("board/<slug>/", board, name="board"),
    path("post/<slug>/", post, name="post")
]
