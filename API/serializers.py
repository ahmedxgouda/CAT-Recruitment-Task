from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        
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
        return data

    def save(self):
        user = User.objects.create_user(username=self.validated_data['username'], email=self.validated_data['email'])
        user.set_password(self.validated_data['password'])
        user.save()
        return user