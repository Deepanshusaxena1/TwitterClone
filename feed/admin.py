from django.contrib import admin

# Register your models here.
from feed.models import Tweet, Comment, Reply, Like

admin.site.register(Tweet)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(Like)

