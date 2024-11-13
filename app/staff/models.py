from django.db import models

from utils.choices import ROLE_CHOICES


class Staff(models.Model):
    user = models.OneToOneField("user.User", on_delete=models.CASCADE)
    staff_type = models.CharField(max_length=20, choices=ROLE_CHOICES)
    # profile fields
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)  # Optional biography field
    is_active = models.BooleanField(default=True)  # Active status, useful for deactivating profiles

    def __str__(self):
        return f'{self.user.username} - {self.staff_type}'
