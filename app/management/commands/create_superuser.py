from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.conf import settings
import os

class Command(BaseCommand):
    help = 'Create a superuser using environment variables'

    def handle(self, *args, **kwargs):
        username = os.getenv('DJANGO_SUPERUSER_USERNAME')
        password = os.getenv('DJANGO_SUPERUSER_PASSWORD')
        email = os.getenv('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')

        if not username or not password:
            self.stdout.write(self.style.ERROR("Environment variables DJANGO_SUPERUSER_USERNAME and DJANGO_SUPERUSER_PASSWORD are required"))
            return

        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.WARNING(f"Superuser with username '{username}' already exists"))
        else:
            User.objects.create_superuser(username=username, password=password, email=email)
            self.stdout.write(self.style.SUCCESS(f"Superuser '{username}' created successfully"))