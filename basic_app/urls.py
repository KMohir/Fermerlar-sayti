from django.urls import path

from basic_app import views
from .views import WorkerProfileListCreate
from .views import NewsList
from .views import CommentListCreateView
from .views import LandDataView
urlpatterns = [
    path('news/', NewsList.as_view(), name='news-list'),  # URL для списка и создания новостей
    path('profiles/', WorkerProfileListCreate.as_view(), name='worker-profile-list-create'),
    path('posts/<int:post_id>/comments/', CommentListCreateView.as_view(), name='post-comments'),
    path('land-data/', LandDataView.as_view(), name='land-data'),
]
