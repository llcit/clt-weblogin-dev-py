# Example use with manage.py:
# $ python manage.py runserver --settings=<projectdir>.settings.dev


from .base import *

# Secret key stored in environment variable not here.
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': PROJECT_DIR.child('db.sqlite3'),
    }
}

AUTHENTICATION_BACKENDS = (
        'django_cas_ng.backends.CASBackend',
    )

CAS_SERVER_URL = 'https://cas-test.its.hawaii.edu/cas/'