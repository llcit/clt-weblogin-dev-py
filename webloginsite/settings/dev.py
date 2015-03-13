# Example use with manage.py:
# $ python manage.py runserver --settings=<projectdir>.settings.dev


from .base import *

import uhauth.tls_patch


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

INSTALLED_APPS += (
	'debug_toolbar',
)

# CAS #

MIDDLEWARE_CLASSES += (
	'django_cas.middleware.CASMiddleware',
)

AUTHENTICATION_BACKENDS = (
		'django.contrib.auth.backends.ModelBackend',
        # 'uhauth.backends.UHCASBackend',
        # 'django_cas.backends.CASBackend',
        
        'uhauth.backends.UHCASAttributesBackend',
)

CAS_SERVER_URL = 'https://cas-test.its.hawaii.edu/cas/'
CAS_VERSION = '2'
CAS_VERSION = 'CAS_2_SAML_1_0'
CAS_REDIRECT_URL = '/'

# END CAS #