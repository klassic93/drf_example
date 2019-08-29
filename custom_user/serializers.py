from rest_framework import serializers
from books.serializers import BookSerializer
from custom_user.models import CustomUser


class CustomUsersDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class CustomUserUpdateSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = CustomUser
        fields = '__all__'
