from rest_framework import permissions, viewsets

from desk.models import ReportDesk
from desk.serializers import ReportDeskSerializer


class ReportDeskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows report desks to be viewed or edited.
    """
    queryset = ReportDesk.objects.all()
    serializer_class = ReportDeskSerializer
    permission_classes = [permissions.IsAuthenticated]
