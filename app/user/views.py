from django.contrib.auth.models import Group, Permission
from rest_framework import permissions
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from staff.serializers import StaffSerializer
from user.models import User
from user.serializers import UserSerializer, GroupSerializer, PermissionSerializer


class RegisterView(APIView):
    http_method_names = ['post']

    """
    API endpoint to create a new user and staff account in one shot.
    """

    def post(self, request, *args, **kwargs):
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user = user_serializer.save()

            staff_data = request.data.copy()
            staff_data['user'] = user.id
            staff_serializer = StaffSerializer(data=staff_data)

            if not staff_serializer.is_valid():
                user.delete()  # delete the created user if staff payload is invalid
                return Response(staff_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            staff_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)

        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class PermissionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Permission.objects.all().order_by('name')
    serializer_class = PermissionSerializer
    permission_classes = [permissions.IsAuthenticated]
