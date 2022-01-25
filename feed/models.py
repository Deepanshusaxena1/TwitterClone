from django.db import models

# Create your models here.
from accounts.models import User


class Tweet(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ID: {self.id} | User ID:{self.user}"

    @staticmethod
    def get_tweet_or_none(tweet_id):
        try:
            tweet_instance = Tweet.objects.get(id=tweet_id)

        except Exception as e:
            tweet_instance = None
            print(e.args)

        return tweet_instance


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, related_name='comments', on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ID: {self.id} | Tweet ID: {self.tweet} | User ID: {self.user}"

    @staticmethod
    def get_comment_or_none(comment_id):
        try:
            comment_instance = Comment.objects.get(id=comment_id)

        except Exception as e:
            comment_instance = None
            print(e.args)

        return comment_instance


class Reply(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ID: {self.id}"


class Media(models.Model):
    id = models.AutoField(primary_key=True)
    file_url = models.CharField(max_length=500, null=True)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ID: {self.id}"


class Like(models.Model):
    id = models.AutoField(primary_key=True)
    tweet = models.ForeignKey(Tweet, related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ID: {self.id}"
