from rest_framework import serializers


from basic_app import models

from .models import News , Comment,LandData

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'heading', 'image', 'published_at', 'text', 'link']

# serializers.py
from rest_framework import serializers
from .models import WorkerProfile

class WorkerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkerProfile
        fields = ['id', 'title', 'name', 'description', 'links', 'pictures']  # Поле pictures добавлено




class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'text', 'created_at']





class LandDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandData
        fields = ['viloyatname','total_area', 'cultivated_area', 'forest_area', 'wasteland_area', 'pastures_area', 'other_agricultural_land']










