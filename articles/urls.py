from django.urls import path
from articles.views import PublicArticleListView, PrivateArticleListView, UserCreateView, ArticleCreateView, \
    ArticleUpdateDeleteView

urlpatterns = [
    path('articles/public/', PublicArticleListView.as_view(), name='public_articles'),
    path('articles/private/', PrivateArticleListView.as_view(), name='private_articles'),
    path('register/', UserCreateView.as_view(), name='register_user'),
    path('articles/create/', ArticleCreateView.as_view(), name='create_article'),
    path('articles/<int:pk>/', ArticleUpdateDeleteView.as_view(), name='edit_delete_article'),
]
