from rest_framework import generics
from custom_user.serializers import CustomUsersDetailSerializer, CustomUserUpdateSerializer
from custom_user.models import CustomUser


class CustomUserListCreateView(generics.ListCreateAPIView):
    serializer_class = CustomUsersDetailSerializer
    queryset = CustomUser.objects.all()


class CustomUserUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CustomUserUpdateSerializer
    queryset = CustomUser.objects.all()
