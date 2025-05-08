from rest_framework import serializers
from .models import FoodMenu, User
from cloudinary import uploader

class RegisterUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'password', 'username']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class CreateListFoodMenuSerializer(serializers.ModelSerializer):
        
    image = serializers.ImageField(write_only = True)
    image_url = serializers.URLField(source='image', read_only = True)

    class Meta:
        model = FoodMenu
        fields = ['name', 'price', 'image', 'image_url']

    def create(self, validated_data):
        
        image = validated_data.pop('image')
        image_url = uploader.upload(image)
        print(image_url['url'])

        return FoodMenu.objects.create(image = image_url['url'], **validated_data) 
