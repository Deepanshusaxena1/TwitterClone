from rest_framework import serializers

from accounts.serializers import UserInfoSerializer
from feed.models import Tweet, Comment, Like


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

    def create(self, validated_data):
        user = validated_data.pop('user')
        tweet = validated_data.pop('tweet')
        tweet_instance = Comment.objects.create(**validated_data, user=user, tweet=tweet)
        return tweet_instance


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'


class TweetSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    likes = LikeSerializer(many=True, read_only=True)
    user = UserInfoSerializer()

    class Meta:
        model = Tweet
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class TweetCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

    def create(self, validated_data):
        user = validated_data.pop('user')
        tweet_instance = Tweet.objects.create(**validated_data, user=user)
        return tweet_instance
