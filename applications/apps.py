# AppConfig is Django's base class for configuring one feature/app.
from django.apps import AppConfig


# This class identifies and configures our `applications` app.
class ApplicationsConfig(AppConfig):
    # If a model does not define an id, Django creates a large auto-incrementing
    # integer primary key for it.
    default_auto_field = 'django.db.models.BigAutoField'

    # This is the Python package name Django should load for this app.
    name = 'applications'
