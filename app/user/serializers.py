from django.contrib.auth.models import Group, Permission
from rest_framework import serializers

from utils.choices import ROLE_CHOICES
from .models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    staff_type = serializers.ChoiceField(choices=ROLE_CHOICES, default='REPORTER')

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'password', 'staff_type']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class PermissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Permission
        fields = ['url', 'name']
