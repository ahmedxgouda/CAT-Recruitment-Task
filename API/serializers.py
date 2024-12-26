from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'role']
        
    def validate(self, data):
        if len(data['password']) < 8:
            raise serializers.ValidationError('Password must be at least 8 characters long')
        if data['password'].isdigit():
            raise serializers.ValidationError('Password must contain at least one letter')
        if data['password'].isalpha():
            raise serializers.ValidationError('Password must contain at least one number')
        if data['password'].islower():
            raise serializers.ValidationError('Password must contain at least one uppercase letter')
        if data['password'].isupper():
            raise serializers.ValidationError('Password must contain at least one lowercase letter')
        if 'role' in data and data['role'] not in ['client', 'admin']:
            raise serializers.ValidationError('Role must be either client or admin')
        if CustomUser.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError('A user with that email already exists.')
        return data

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user
    