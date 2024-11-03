from django.db import models
from django_quill.fields import QuillField

# Create your models here.


class News(models.Model):
    heading = models.CharField(max_length=200, null=True, blank=True)  # Укажите значение по умолчанию
    image = models.ImageField(upload_to='news_images/')
    published_at = models.DateTimeField(auto_now_add=True)
    text = QuillField()
    link = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.heading
# models.py
from django.db import models
from django.contrib.postgres.fields import ArrayField

class WorkerProfile(models.Model):
    title = models.CharField(max_length=255)           # Заголовок
    name = models.CharField(max_length=100)            # Имя сотрудника
    description = models.TextField()                   # Описание
    links = models.URLField(max_length=200, blank=True, null=True)
    # links = models.JSONField(default=dict)             # Ссылки (JSON)
    pictures=models.URLField(max_length=200, blank=True, null=True)
    # pictures = ArrayField(models.ImageField(upload_to='worker_images/'), blank=True, null=True)  # Поле для нескольких изображений

    def __str__(self):
        return self.title

    def __str__(self):
        return self.title


# models.py
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # другие поля...

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    author = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post.title}"






class LandData(models.Model):
    viloyatname=models.CharField(max_length=255)
    total_area = models.CharField(max_length=50)
    cultivated_area = models.CharField(max_length=50)
    forest_area = models.CharField(max_length=50)
    wasteland_area = models.CharField(max_length=50)
    pastures_area = models.CharField(max_length=50)
    other_agricultural_land = models.CharField(max_length=50)

    def __str__(self):
        return f"Land Data {self.id}"






