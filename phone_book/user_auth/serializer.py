# user_auth/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User


# user_auth/serializers.py

from rest_framework import serializers

class UserRegistrationSerializer(serializers.Serializer):
    # Add fields and logic here
    pass
class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords must match."})
        return attrs

    def create(self, validated_data):
        # Remove password2 since it's just for confirmation
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user