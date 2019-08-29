from django.urls import path
from custom_user.views import *

urlpatterns = [
    path('users/', CustomUserListCreateView.as_view()),
    path('users/<int:pk>/', CustomUserUpdateView.as_view()),
]
