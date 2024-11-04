from django.core.management import call_command

def create_superuser_after_migrate(sender, **kwargs):
    # Вызов кастомной команды для создания суперпользователя
    call_command('createsuperuser')

