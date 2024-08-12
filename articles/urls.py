from django.urls import path
from .views import PublicArticleListView, PrivateArticleListView, ArticleCreateView, UserCreateView

urlpatterns = [
    path('articles/', PublicArticleListView.as_view(), name='public_articles'),
    path('articles/private/', PrivateArticleListView.as_view(), name='private_articles'),
    path('articles/create/', ArticleCreateView.as_view(), name='create_article'),
    path('register/', UserCreateView.as_view(), name='register_user'),
]
