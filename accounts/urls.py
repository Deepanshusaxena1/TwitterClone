from django.urls import path

from accounts.views import FollowView, FetchUserView, CreateUserView, FetchUserWithEmailView

urlpatterns = [
    path('follow', FollowView.as_view(), name='follow-user'),
    path('user/fetch', FetchUserView.as_view(), name='fetch-user'),
    path('user/fetch_with_email', FetchUserWithEmailView.as_view(), name='fetch-user-with-email'),
    path('user/create', CreateUserView.as_view(), name='create-user')
]
