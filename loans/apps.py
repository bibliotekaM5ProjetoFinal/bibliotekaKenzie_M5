from django.apps import AppConfig
from schedules import updater
import os
class LoansConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "loans"

    def ready(self) -> None:
        if os.environ.get('RUN_MAIN'):
            updater.start()
        