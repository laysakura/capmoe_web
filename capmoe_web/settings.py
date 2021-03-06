"""
Django settings for capmoe_web project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = open(os.path.join(BASE_DIR, 'capmoe_web', 'password', 'django-secret-key')).read().strip(),

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_nose',
    'capmoe_app',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'capmoe_web.urls'

WSGI_APPLICATION = 'capmoe_web.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE'   : 'django.db.backends.mysql',
        'NAME'     : 'capmoe',
        'USER'     : 'capmoeuser',
        'PASSWORD' : open(os.path.join(BASE_DIR, 'capmoe_web', 'password', 'mysql-capmoeuser-pass')).read().strip(),
        'HOST'     : '127.0.0.1',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Japan'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Templates

TEMPLATE_DIRS = [
    os.path.join(BASE_DIR, 'capmoe_app', 'templates'),
]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'


# Logger
import sys
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': ('[%(asctime)s] %(filename)s '
                       '%(funcName)s():%(lineno)d\t%(message)s'),
        },
    },
    'handlers': {
        'rainbow': {
            'level'     : 'DEBUG',
            'class'     : 'rainbow_logging_handler.RainbowLoggingHandler',
            'formatter' : 'verbose',
            'stream'    : sys.stderr,
        },
    },
    'loggers': {
        '': {
            'handlers'  : ['rainbow'],
            'level'     : 'DEBUG',
            'propagate' : True,
        },
    },
}


# Unit test
# Using django_nose => https://github.com/django-nose/django-nose

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
    '--verbosity=2',
    '--nocapture',
    '--detailed-errors',
    '--with-doctest',
    '--with-cov',
    '--cov=capmoe_app',
    '--cov-config=.coveragerc',
    '--cov-report=html',
]
