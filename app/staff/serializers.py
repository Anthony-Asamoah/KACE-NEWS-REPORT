from django.contrib.auth.models import Group
from rest_framework import serializers

from utils.choices import STAFF_TYPE_TO_GROUP
from .models import Staff


class StaffSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=100, required=False, allow_blank=True)
    last_name = serializers.CharField(max_length=100, required=False, allow_blank=True)
    phone_number = serializers.CharField(max_length=15, required=False, allow_blank=True)
    address = serializers.CharField(required=False, allow_blank=True)
    date_of_birth = serializers.DateField(required=False, allow_null=True)
    profile_picture = serializers.ImageField(required=False, allow_null=True)
    bio = serializers.CharField(required=False, allow_blank=True)
    is_active = serializers.BooleanField(default=True)

    class Meta:
        model = Staff
        fields = [
            'user',
            'staff_type',
            'first_name',
            'last_name',
            'phone_number',
            'address',
            'date_of_birth',
            'profile_picture',
            'bio',
            'is_active'
        ]

    def create(self, validated_data):
        user = validated_data.pop('user')
        staff = Staff.objects.create(user=user, **validated_data)

        # Assign the group based on staff_type
        staff_type = validated_data.get('staff_type', 'REPORTER')
        group_name = STAFF_TYPE_TO_GROUP.get(staff_type)
        if group_name:
            group, created = Group.objects.get_or_create(name=group_name)
            user.groups.add(group)

        return staff
