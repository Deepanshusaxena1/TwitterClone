# Create your views here.
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


from rest_framework import status as status_codes
from rest_framework.views import APIView

from accounts.models import Follow, User
from feed.constants import Constants
from feed.models import Tweet, Comment
from feed.serializers import TweetSerializer, CommentSerializer, LikeSerializer, TweetCreateSerializer
from feed.utility import RequestUtilities, TimeUtilities


class FetchTweetView(APIView):

    def get(self, request):
        tweet_id = request.GET.get('tweet_id')

        if not tweet_id:
            return JsonResponse({'error_message': "Invalid parameter: tweet_id"},
                                status=status_codes.HTTP_400_BAD_REQUEST)

        tweet_instance = Tweet.get_tweet_or_none(tweet_id)

        if not tweet_instance:
            return JsonResponse({'error_message': "Tweet not found."}, status=status_codes.HTTP_400_BAD_REQUEST)

        tweet_serializer = TweetSerializer(tweet_instance).data
        return JsonResponse({'tweet_data': tweet_serializer}, status=status_codes.HTTP_200_OK)


class CreateTweetView(APIView):

    @method_decorator(csrf_exempt)
    def post(self, request):
        req_body = RequestUtilities.load_request_body(request)

        tweet_serializer = TweetCreateSerializer(data=req_body)

        if tweet_serializer.is_valid():
            tweet_serializer.save()

        else:
            return JsonResponse({'error_message': tweet_serializer.errors}, status=status_codes.HTTP_400_BAD_REQUEST)

        return JsonResponse({'tweet_data': tweet_serializer.data}, status=status_codes.HTTP_200_OK)


class FetchCommentView(APIView):

    def get(self, request):
        comment_id = request.GET.get('comment_id')

        if not comment_id:
            return JsonResponse({'error_message': "Invalid parameter: comment_id"},
                                status=status_codes.HTTP_400_BAD_REQUEST)

        comment_instance = Comment.get_comment_or_none(comment_id)

        if not comment_instance:
            return JsonResponse({'error_message': "Comment not found."})

        comment_serializer = CommentSerializer(comment_instance).data
        return JsonResponse({'comment_data': comment_serializer}, status=status_codes.HTTP_200_OK)


class CreateCommentView(APIView):

    def post(self, request):
        req_body = RequestUtilities.load_request_body(request)

        comment_serializer = CommentSerializer(data=req_body)

        if comment_serializer.is_valid():
            comment_serializer.save()

        else:
            return JsonResponse({'error_message': comment_serializer.errors}, status=status_codes.HTTP_400_BAD_REQUEST)

        return JsonResponse({'comment_data': comment_serializer.data}, status=status_codes.HTTP_200_OK)


class FetchCommentsView(APIView):

    def get(self, request):
        tweet_id = request.GET.get('tweet_id')

        if not tweet_id:
            return JsonResponse({'error_message': "Invalid parameter: tweet_id"},
                                status=status_codes.HTTP_400_BAD_REQUEST)

        tweet_instance = Tweet.get_tweet_or_none(tweet_id)

        if not tweet_instance:
            return JsonResponse({'error_message': "Tweet not found."}, status=status_codes.HTTP_400_BAD_REQUEST)

        comments_filter = Comment.objects.filter(tweet_id=tweet_id)

        if not comments_filter:
            return JsonResponse({'error_message': "No Comments on this tweet so far."},
                                status=status_codes.HTTP_400_BAD_REQUEST)

        comment_serializers = CommentSerializer(comments_filter, many=True).data
        return JsonResponse({'comments': comment_serializers}, status=status_codes.HTTP_200_OK)


class FetchFeedView(APIView):

    def get(self, request):
        user_id = request.GET.get('user_id')

        if not user_id:
            return JsonResponse({'error_message': "Invalid parameter: user_id"},
                                status=status_codes.HTTP_400_BAD_REQUEST)
        try:
            user_instance = User.objects.get(id=user_id)

        except Exception as e:
            print(e)
            user_instance = None

        if not user_instance:
            return JsonResponse({'error_message': "User not found."}, status=status_codes.HTTP_400_BAD_REQUEST)

        following_user_ids = list(Follow.objects.filter(follower_id=user_id).values_list('following_id', flat=True))

        tweet_filter = Tweet.objects.filter(user_id__in=following_user_ids,
                                            created_at__gte=TimeUtilities.get_past_time_from_now(Constants.FEED_HOURS),
                                            is_deleted=False).order_by('-created_at')

        tweet_serializer = TweetSerializer(tweet_filter, many=True).data
        return JsonResponse({'tweets': tweet_serializer}, status=status_codes.HTTP_200_OK)


class LikeView(APIView):

    def post(self, request):
        req_body = RequestUtilities.load_request_body(request)

        like_serializer = LikeSerializer(data=req_body)

        if like_serializer.is_valid():
            like_serializer.save()

        else:
            return JsonResponse({'error_message': like_serializer.errors}, status=status_codes.HTTP_400_BAD_REQUEST)

        return JsonResponse({'like_status': like_serializer.data}, status=status_codes.HTTP_200_OK)
