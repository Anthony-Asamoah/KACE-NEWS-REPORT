from django.db import models


class ReportDesk(models.Model):
    report = models.ForeignKey(
        "report.Report",
        on_delete=models.CASCADE
    )
    desk_head = models.ForeignKey(
        "staff.Staff",
        on_delete=models.CASCADE,
        related_name='desk_head'
    )
    zonal_editor = models.ForeignKey(
        "staff.Staff",
        on_delete=models.CASCADE,
        related_name='zonal_editor',
        null=True,
        blank=True
    )
    regional_editor = models.ForeignKey(
        "staff.Staff",
        on_delete=models.CASCADE,
        related_name='regional_editor',
        null=True,
        blank=True
    )
    national_editor = models.ForeignKey(
        "staff.Staff",
        on_delete=models.CASCADE,
        related_name='national_editor',
        null=True,
        blank=True
    )
    assigned_at = models.DateTimeField(auto_now_add=True)
    reviewed_at = models.DateTimeField(null=True, blank=True)
    approved_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'Report {self.report.title} - Desk Head: {self.desk_head.user.username}'
