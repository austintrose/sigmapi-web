# DEVELOPMENT settings for Sigma Pi website.

import os
from . import environment_settings

# These are settings which must change, depending on whether this is development
# or production. So, we store them in a separate file.
DEBUG = environment_settings.DEBUG
ADMINS = environment_settings.ADMINS
DATABASES = environment_settings.DATABASES
ALLOWED_HOSTS = environment_settings.ALLOWED_HOSTS
DOWNLOADVIEW_BACKEND = environment_settings.DOWNLOADVIEW_BACKEND
MEDIA_ROOT = environment_settings.MEDIA_ROOT
STATIC_ROOT = environment_settings.STATIC_ROOT
STATICFILES_DIRS = environment_settings.STATICFILES_DIRS
SECRET_KEY = environment_settings.SECRET_KEY
EMAIL_HOST = environment_settings.EMAIL_HOST
EMAIL_PORT = environment_settings.EMAIL_PORT
EMAIL_HOST_USER = environment_settings.EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = environment_settings.EMAIL_HOST_PASSWORD
DEFAULT_FROM_EMAIL = environment_settings.DEFAULT_FROM_EMAIL
SERVER_EMAIL = environment_settings.SERVER_EMAIL


#TEMPLATE_CONTEXT_PROCESSORS += ('django.core.context_processors.request',)

BASE_DIR = os.getcwd()

EC_EMAIL = "sigmapi@wpi.edu"
ACTIVES_EMAIL = "sigmapiactives@wpi.edu"
ALUMNI_EMAIL = "sigmapialumni@wpi.edu"

MANAGERS = ADMINS




# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = False

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/content/'

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/secure/'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
        ],
        'APP_DIRS': True,
        'OPTIONS': {'context_processors' : [
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth'
            ]
        }

    }
]

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    #These two things may be the same, but django is warning to add the second one
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_downloadview.SmartDownloadMiddleware'
)

DOWNLOADVIEW_RULES = [
    {
        'destination_dir': 'lightpd-optimized-by-middleware'
    }
]

ROOT_URLCONF = 'SigmaPi.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'SigmaPi.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'PubSite',
    'UserInfo',
    'Archive',
    'PartyList',
    'Secure',
    'Links',
    'Standards',
    'Scholarship',
)

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
