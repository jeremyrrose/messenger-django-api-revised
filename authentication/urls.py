from django.conf.urls import url, include
from authentication.views import RegistrationAPIView, LoginAPIView, UserListViewSet, SingleUser

urlpatterns = [
    url(r'^users/$', UserListViewSet.as_view({'get': 'list'}), name='user_list'),
    url(r'^users/register/$', RegistrationAPIView.as_view(), name='register'),
    url(r'^users/login/$', LoginAPIView.as_view(), name='login'),
    url(r'^users/user/$', SingleUser.as_view(), name='user'),
]
