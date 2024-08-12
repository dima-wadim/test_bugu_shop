from rest_framework import generics, permissions
from .models import Article
from .serializers import ArticleSerializer, UserSerializer
from django.contrib.auth.models import User

class PublicArticleListView(generics.ListAPIView):
    queryset = Article.objects.filter(is_private=False)
    serializer_class = ArticleSerializer

class PrivateArticleListView(generics.ListAPIView):
    queryset = Article.objects.filter(is_private=True)
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated]

class ArticleCreateView(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
