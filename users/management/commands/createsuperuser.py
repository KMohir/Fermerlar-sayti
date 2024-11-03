from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'Create a superuser with login=admin and password=admin123 if it does not exist'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                password='admin123'
            )
            self.stdout.write(self.style.SUCCESS('Superuser "admin" created successfully!'))

        else:
            self.stdout.write(self.style.WARNING('Superuser "admin" already exists.'))
