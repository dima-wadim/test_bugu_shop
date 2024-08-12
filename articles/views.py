from rest_framework import generics, permissions
from .models import Article, CustomUser
from .serializers import ArticleSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class PublicArticleListView(generics.ListAPIView):
    queryset = Article.objects.filter(is_public=True)
    serializer_class = ArticleSerializer
    permission_classes = [permissions.AllowAny]

class PrivateArticleListView(generics.ListAPIView):
    queryset = Article.objects.filter(is_public=False)
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]

class UserCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class ArticleCreateView(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class ArticleUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAdminUser]

    def perform_update(self, serializer):
        if self.request.user == self.get_object().author:
            serializer.save()

    def perform_destroy(self, instance):
        if self.request.user == instance.author:
            instance.delete()
