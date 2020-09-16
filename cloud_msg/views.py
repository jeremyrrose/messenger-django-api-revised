from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.exceptions import (
    ValidationError, PermissionDenied
)
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Message
from .serializers import MessageSerializer


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
