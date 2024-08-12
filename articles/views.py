from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Article
from .serializers import ArticleSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'DELETE']:
            return [IsAdminUser()]
        if self.request.method == 'POST':
            return [IsAuthenticated()]
        return super().get_permissions()
