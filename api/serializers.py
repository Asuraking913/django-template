from rest_framework import serializers

class BaseViewSerializer(serializers.Serializer):

    name = serializers.CharField()