from rest_framework import serializers
from .models import Message, UserProfile
# from django.contrib.auth.models import User, Group
from authentication.models import User


# SERIALIZERS CONVERT BETWEEN DJANGO AND JSON FORMAT AND
# ALLOWS FIELDS OF YOUR MODEL TO BE DISPLAYED TO YOUR USER
class MessageSerializer(serializers.ModelSerializer):
    sender_name = serializers.ReadOnlyField(source='sender.username')
    receiver_name = serializers.ReadOnlyField(source='receiver.username')
    # receiver = serializers.CharField(source='receiver.username')
    # receiver = serializers.CharField(source='receiver.username')
    # conversations = ConversationSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Message
        fields = ('id', 'sender_name', 'sender', 'receiver_name', 'receiver', 'message',
                  'timestamp', 'last_update_at', 'is_read')


class UserProfileSerializer(serializers.ModelSerializer):
    # id = serializers.ReadOnlyField(source='user.id')
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = UserProfile
        fields = ('id', 'user', 'avatar',
                  'timestamp', 'last_update_at')
