# Create your views here.
from django.http import JsonResponse
from rest_framework import status as status_codes
from rest_framework.views import APIView

from accounts.models import User
from accounts.serializers import FollowSerializer, UserInfoSerializer
from feed.utility import RequestUtilities


class FollowView(APIView):

    def post(self, request):
        req_body = RequestUtilities.load_request_body(request)

        follow_serializer = FollowSerializer(data=req_body)

        if follow_serializer.is_valid():
            follow_serializer.save()

        else:
            return JsonResponse({'error_message': follow_serializer.errors}, status=status_codes.HTTP_400_BAD_REQUEST)

        return JsonResponse({'followed_status': follow_serializer.data}, status=status_codes.HTTP_200_OK)


class FetchUserView(APIView):

    def get(self, request):
        user_id = request.GET.get("user_id", None)

        if not user_id:
            return JsonResponse({"error_message": "Invalid User ID"})

        try:
            user_instance = User.objects.get(id=user_id)

        except Exception as e:
            print(e.args)
            user_instance = None

        if not user_instance:
            return JsonResponse({"error_message": "User Not Found"})

        user_serializer = UserInfoSerializer(user_instance, many=False).data

        return JsonResponse({'user_data': user_serializer}, status=status_codes.HTTP_200_OK)


class CreateUserView(APIView):

    def post(self, request):
        req_body = RequestUtilities.load_request_body(request)

        user_serializer = UserInfoSerializer(data=req_body)

        if user_serializer.is_valid():
            user_serializer.save()

        else:
            return JsonResponse({'error_message': user_serializer.errors}, status=status_codes.HTTP_400_BAD_REQUEST)

        return JsonResponse({'user_data': user_serializer.data}, status=status_codes.HTTP_200_OK)


class FetchUserWithEmailView(APIView):

    def get(self, request):
        email = request.GET.get("email", None)

        if not email:
            return JsonResponse({"error_message": "Invalid User E-Mail"})

        try:
            user_instance = User.objects.get(email=email)

        except Exception as e:
            print(e.args)
            user_instance = None

        if not user_instance:
            return JsonResponse({"error_message": "User Not Found"})

        user_serializer = UserInfoSerializer(user_instance, many=False).data

        return JsonResponse({'user_data': user_serializer}, status=status_codes.HTTP_200_OK)
