from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        search = self.request.query_params.get('search', '')
        if search:
            qs = qs.filter(message__icontains=search)

        return qs
