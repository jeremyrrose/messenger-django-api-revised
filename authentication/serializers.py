from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import User


class RegistrationSerializer(serializers.ModelSerializer):
    """Serializers registration requests and creates a new user."""

    password = serializers.CharField(
        max_length=255,
        min_length=8,
        write_only=True
    )
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        # List all of the fields that could possibly be included in a request
        # or response
        fields = ('username', 'email', 'first_name', 'last_name', 'password', 'token')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class ProfileIdField(serializers.ReadOnlyField):
    """
    hacky solution to return profile id on login for users with profiles
    """
    def to_representation(self, value):
        return value

class LoginSerializer(serializers.ModelSerializer):
    """Serializer login requests and signin user"""
    # id = serializers.ReadOnlyField(max_length=255, read_only=True)
    email = serializers.CharField(max_length=255, read_only=True)
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)
    profile = ProfileIdField(read_only=True, required=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'token', 'profile')

    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)

        # Raise an exception if a
        # username is not provided.
        if username is None:
            raise serializers.ValidationError(
                'A username is required to login'
            )
        # Raise an exception if a
        # password is not provided.
        if password is None:
            raise serializers.ValidationError(
                'A password is required to login'
            )
        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError(
                'A user with that username or password was not found'
            )
        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated'
            )
        try:
            profile = user.profile.id
        except:
            profile = None

        return {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "token": user.token,
            "profile": profile
        }

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


