from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import UserSerializer
from .permissions import IsAdmin, IsOwner
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser
# Create your views here.

class GetUsers(ListAPIView):
    permission_classes = [IsAuthenticated, IsAdmin]
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()

class Register(CreateAPIView):
    permission_classes = []
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    
class GetUser(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsAdmin | IsOwner]
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    