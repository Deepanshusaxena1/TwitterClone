from django.urls import path

from feed.views import FetchTweetView, FetchCommentsView, CreateTweetView, FetchCommentView, CreateCommentView, \
    FetchFeedView, LikeView

urlpatterns = [
    path('tweet/fetch', FetchTweetView.as_view(), name='fetch-tweet'),
    path('tweet/create', CreateTweetView.as_view(), name='create-tweet'),
    path('comment/fetch', FetchCommentView.as_view(), name='fetch-comment'),
    path('comment/create', CreateCommentView.as_view(), name='create-comment'),
    path('tweet/fetch_comments', FetchCommentsView.as_view(), name='fetch-tweet-comments'),
    path('fetch', FetchFeedView.as_view(), name='fetch-feed'),
    path('tweet/like', LikeView.as_view(), name='create-like'),
]

