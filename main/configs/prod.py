import os

SECRET_KEY = os.environ["DJANGO_SECRET_KEY"].strip()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': os.environ["DJANGO_DB_HOST"].strip(),
        'PORT': os.environ["DJANGO_DB_PORT"].strip(),
        'NAME': os.environ["DJANGO_DB_NAME"].strip(),
        'USER': os.environ["DJANGO_DB_USER"].strip(),
        'PASSWORD': os.environ["DJANGO_DB_PASS"].strip(),
        'OPTIONS': {
            'charset': os.environ["DJANGO_DB_CHARSET"].strip(),
            'use_unicode': True,
        },
    }
}

# Email
EMAIL_BACKEND       = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST          = os.environ["DJANGO_EMAIL_HOST"].strip()
EMAIL_PORT          = os.environ["DJANGO_EMAIL_PORT"].strip()
EMAIL_HOST_USER     = os.environ["DJANGO_EMAIL_USER"].strip()
EMAIL_HOST_PASSWORD = os.environ["DJANGO_EMAIL_PASSWORD"].strip()
EMAIL_USE_TLS       = os.environ["DJANGO_EMAIL_TLS"].strip()

# Source mail
DEFAULT_FROM_EMAIL  = os.environ["DJANGO_EMAIL_FROM"].strip()

# Media
MEDIA_URL           = os.environ["DJANGO_MEDIA_URL"].strip()
MEDIA_ROOT          = os.environ["DJANGO_MEDIA_ROOT"].strip()

# Google analytics
GOOGLE_ANALYTICS_KEY = os.environ.get("GOOGLE_ANALYTICS_KEY").strip()
