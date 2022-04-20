import os
from pathlib import Path

SECRET_KEY = "this_is_dev_secret_key"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(
            Path(__file__).resolve().parent.parent.parent,
            'db.sqlite3'
            ),
    }
}

# Email test environnement

EMAIL_BACKEND   = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST_USER = "john.doe@fake.com"

# Media
MEDIA_URL   = "/media/"
MEDIA_ROOT  = os.path.join(
    Path(__file__).resolve().parent.parent.parent,
    "media"
    )

# google_analytics
GOOGLE_ANALYTICS_KEY = ""
