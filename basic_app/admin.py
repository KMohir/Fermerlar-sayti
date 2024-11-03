from django.contrib import admin

from basic_app.models import News,WorkerProfile,Post, Comment

# Register your models here.

admin.site.register(News)
admin.site.register(WorkerProfile)

admin.site.register(Post)
admin.site.register(Comment)
