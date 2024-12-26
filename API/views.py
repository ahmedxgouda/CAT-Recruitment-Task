from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from .serializers import UserSerializer
from .permissions import IsAdmin, IsOwner
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
# Create your views here.

class GetUsers(ListAPIView):
    permission_classes = [IsAuthenticated, IsAdmin]
    serializer_class = UserSerializer
    queryset = User.objects.all()

class Register(CreateAPIView):
    permission_classes = []
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
class GetUser(RetrieveAPIView):
    permission_classes = [IsAuthenticated, IsAdmin | IsOwner]
    serializer_class = UserSerializer
    queryset = User.objects.all()
    