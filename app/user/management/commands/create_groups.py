from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create groups based on ROLE_CHOICES"

    def handle(self, *args, **kwargs):
        from utils.choices import ROLE_CHOICES

        for role_code, role_name in ROLE_CHOICES:
            group, created = Group.objects.get_or_create(name=role_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Group '{role_name}' created successfully"))
            else:
                self.stdout.write(self.style.SUCCESS(f"Group '{role_name}' already exists"))
