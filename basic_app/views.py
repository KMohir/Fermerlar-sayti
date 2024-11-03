
from basic_app.models import *
from basic_app.serializers import *

from rest_framework import generics
from .models import WorkerProfile
from .serializers import WorkerProfileSerializer






from .models import News
from .serializers import NewsSerializer

class NewsList(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

# views.py

class WorkerProfileListCreate(generics.ListCreateAPIView):
    queryset = WorkerProfile.objects.all()
    serializer_class = WorkerProfileSerializer

# views.py
from rest_framework import generics
from .models import Comment
from .serializers import CommentSerializer

class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        # Получить все комментарии для указанного поста
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post_id=post_id)

    def perform_create(self, serializer):
        # Сохранить комментарий с указанным постом
        post_id = self.kwargs['post_id']
        serializer.save(post_id=post_id)


# views.py
from rest_framework import generics
from .models import LandData
from .serializers import LandDataSerializer

class LandDataView(generics.ListAPIView):
    queryset = LandData.objects.all()
    serializer_class = LandDataSerializer



