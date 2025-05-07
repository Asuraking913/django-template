from rest_framework import serializers
from .models import User

class RegisterUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'password', 'username']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)