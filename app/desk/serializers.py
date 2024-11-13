from rest_framework import serializers

from desk.models import ReportDesk


class ReportDeskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ReportDesk
        fields = [
            'url',
            'report',
            'desk_head',
            'zonal_editor',
            'regional_editor',
            'national_editor',
            'reviewed_at',
            'approved_at',
        ]
