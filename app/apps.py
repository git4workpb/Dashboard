from django.apps import AppConfig
from .scheduler import start_scheduler


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

    def ready(self):
        start_scheduler()