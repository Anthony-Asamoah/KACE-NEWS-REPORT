from rest_framework import serializers

from report.models import Report


class ReportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Report
        fields = [
            'url',
            'title',
            'content',
            'status',
            'tags',
            'category',
            'category_specific_fields',
            'attachments',
            'created_at',
            'updated_at',
            'geo_latitude',
            'geo_longitude',
        ]
