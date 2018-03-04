from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.is_superuser = False
        user.save()
        return user