from django.apps import AppConfig
class LoansConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "loans"

    def ready(self) -> None:
        from schedules import updater
        import os
        
        if os.environ.get('RUN_MAIN'):
            updater.start()
        