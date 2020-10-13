from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import viewsets, views
from rest_framework.exceptions import (
    ValidationError, PermissionDenied
)
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Message, UserProfile
from .serializers import MessageSerializer, UserProfileSerializer


#
# Create your views here.
class MessageViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = MessageSerializer

    def get_queryset(self):
        queryset = Message.objects.all().filter(sender=self.request.user) | \
                   Message.objects.all().filter(receiver=self.request.user)
        return queryset

    def create(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            raise PermissionDenied(
                "Only logged in users with accounts can create recipes"
            )
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)


# class ConversationViewSet(viewsets.ModelViewSet):
#     permission_classes = (IsAuthenticated,)
#     serializer_class = MessageSerializer
#
#     def get_queryset(self):
#         queryset = Message.objects.all().filter(sender=self.request.user) |\
#                    Message.objects.all().filter(receiver=self.request.user)
#         return queryset


class UserProfileViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        return UserProfile.objects.all()
        # self.request.user, self.request.avatar
        # UserProfile.objects.all()

    def create(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            raise PermissionDenied(
                "Only logged in users with accounts can create recipes"
            )
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        # userprofile = UserProfile.objects.get(pk=self.kwargs["pk"])
        return super().destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        userprofile = UserProfile.objects.get(pk=self.kwargs["pk"])
        return super().update(request, *args, **kwargs)


class UserSearch(views.APIView):

    permission_classes = (AllowAny,)
    serializer_class = UserProfileSerializer

    def get(self, request, *args, **kwargs):
        search_string = kwargs.get('search_string')
        if search_string:
            users = UserProfile.objects.filter(user__username__icontains=search_string)
            serializer = UserProfileSerializer(users, many=True)
            print(users)
            return Response(serializer.data)

