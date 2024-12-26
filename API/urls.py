from django.urls import path
from .views import GetUsers, Register, GetUser
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('users', GetUsers.as_view()),
    path('auth/register', Register.as_view()),
    path('users/<int:pk>', GetUser.as_view()),
    path('auth/login', TokenObtainPairView.as_view()),
    path('auth/refresh', TokenRefreshView.as_view())
]
