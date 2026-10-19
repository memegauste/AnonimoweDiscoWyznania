"""Configure the designation storage application."""

# Django
from django.apps import AppConfig


class StorageConfig(AppConfig):
    """Register the storage application with Django."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'backend.storage'
