from .default import *
import os
SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = 0

ALLOWED_HOSTS += os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")
CSRF_TRUSTED_ORIGINS = ["http://localhost:1337"]
INTERNAL_IPS = [
    "127.0.0.1",
]

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("SQL_DATABASE", BASE_DIR / "db.sqlite3"),
        "USER": os.environ.get("SQL_USER", "user"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
        "HOST": os.environ.get("SQL_HOST", "localhost"),
        "PORT": os.environ.get("SQL_PORT", "5432"),
    }
}
print(ALLOWED_HOSTS)