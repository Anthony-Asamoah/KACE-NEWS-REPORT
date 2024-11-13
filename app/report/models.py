from django.db import models

from utils.choices import STATUS_CHOICES


class Report(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='DRAFT')
    tags = models.ManyToManyField('common.Tag', related_name='reports')
    category = models.ForeignKey('common.Category', on_delete=models.CASCADE)
    category_specific_fields = models.JSONField(default=dict)
    attachments = models.ManyToManyField('common.Attachment', related_name='reports')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    geo_latitude = models.FloatField(null=True, blank=True)
    geo_longitude = models.FloatField(null=True, blank=True)


def __str__(self):
    return self.title
