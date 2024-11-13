from rest_framework import permissions, viewsets

from staff.models import Staff
from staff.serializers import StaffSerializer


class StaffViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows staffs to be viewed or edited.
    """
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = [permissions.IsAuthenticated]
