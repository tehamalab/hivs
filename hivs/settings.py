"""
Django settings for hivs project.

Generated by 'django-admin startproject' using Django 2.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import dotenv
from .utils import sbool


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

dotenv.load_dotenv(os.path.join(BASE_DIR, ".env"))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 's3cr3t-K3y')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = sbool(os.environ.get('DEBUG', 'false'))

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*').split()

INTERNAL_IPS = os.environ.get('INTERNAL_IPS', '127.0.0.1').split()


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.gis',
    'compressor',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'import_export',
    'mptt',
    'django_mptt_admin',
    'phonenumber_field',
    'django_postgres_utils',
    'crispy_forms',
    'rest_framework',
    'rest_framework_gis',
    'django_filters',
    'rangefilter',
    'hivs_utils',
    'hivs_users',
    'hivs_dash',
    'hivs_administrative',
    'hivs_clients',
    'hivs_pp',
    'hivs_htc',
    'hivs_cd',
    'debug_toolbar',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hivs.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': os.environ.get('TEMPLATES_DIRS', os.path.join(BASE_DIR, 'templates')).split(),
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'hivs.context_processors.site',
            ],
        },
    },
]

WSGI_APPLICATION = 'hivs.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DATABASE_ENGINE', 'django.contrib.gis.db.backends.postgis'),
        'NAME': os.environ.get('DATABASE_NAME', 'hivs'),
        'USER': os.environ.get('DATABASE_USER', 'hivs'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', 'hivs'),
        'HOST': os.environ.get('DATABASE_HOST', 'localhost'),
        'PORT': os.environ.get('DATABASE_PORT', '5432'),
        'CONN_MAX_AGE': int(os.environ.get('DATABASE_CONN_MAX_AGE', 0)),
        'ATOMIC_REQUESTS': sbool(os.environ.get('DATABESE_ATOMIC_REQUESTS', 'true')),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_USER_MODEL = os.environ.get('AUTH_USER_MODEL', 'hivs_users.User')

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
]

LOGIN_URL = os.environ.get('LOGIN_URL', 'account_login')

LOGIN_REDIRECT_URL = os.environ.get('LOGIN_REDIRECT_URL', '/')

ACCOUNT_ADAPTER = 'hivs.account_adapter.AccountAdapter'

ACCOUNT_OPEN_FOR_SIGNUP = sbool(os.environ.get('ACCOUNT_OPEN_FOR_SIGNUP', 'false'))

ACCOUNT_DEFAULT_HTTP_PROTOCOL = os.environ.get('ACCOUNT_DEFAULT_HTTP_PROTOCOL', 'https')

ACCOUNT_SESSION_REMEMBER = sbool(os.environ.get('ACCOUNT_SESSION_REMEMBER', 'false'))

ACCOUNT_AUTHENTICATION_METHOD = os.environ.get('ACCOUNT_AUTHENTICATION_METHOD', 'username_email')


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = os.environ.get('LANGUAGE_CODE', 'en-us')

TIME_ZONE = os.environ.get('TIME_ZONE', 'UTC')

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

STATIC_URL = os.environ.get('STATIC_URL', '/static/')

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

STATIC_ROOT = os.environ.get('STATIC_ROOT', os.path.join(BASE_DIR, 'static_root'))

MEDIA_URL = os.environ.get('MEDIA_URL', '/media/')

MEDIA_ROOT = os.environ.get('MEDIA_ROOT', os.path.join(BASE_DIR, 'media_root'))

# Site

SITE_ID = int(os.environ.get('SITE_ID', 1))

SITE_NAME = os.environ.get('SITE_NAME', 'Hivs')

SITE_TAGLINE = os.environ.get('SITE_TAGLINE', 'Data Management')

ADMIN_SITE_NAME = os.environ.get('ADMIN_SITE_HEADER', SITE_NAME)

ADMIN_SITE_HEADER = os.environ.get('ADMIN_SITE_HEADER', SITE_NAME)

ADMIN_INDEX_TITLE = os.environ.get('ADMIN_INDEX_TITLE', 'Administration and Data management')

# API

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.DjangoModelPermissions',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
    'DEFAULT_FILTER_BACKENDS': [
        'rest_framework.filters.OrderingFilter',
        'django_filters.rest_framework.DjangoFilterBackend',
    ]
}

# Session

SESSION_COOKIE_AGE = int(os.environ.get('SESSION_COOKIE_AGE', '3600'))

SESSION_EXPIRE_AT_BROWSER_CLOSE = sbool(os.environ.get('SESSION_EXPIRE_AT_BROWSER_CLOSE', 'true'))

if os.environ.get('SESSION_COOKIE_SECURE', None):
    SESSION_COOKIE_SECURE = sbool(os.environ.get('SESSION_COOKIE_SECURE', 'false'))

# SSL

if os.environ.get('SECURE_PROXY_SSL_HEADER', None):
    SECURE_PROXY_SSL_HEADER = os.environ.get('SECURE_PROXY_SSL_HEADER').split()[:2]

if os.environ.get('SECURE_SSL_REDIRECT', None):
    SECURE_SSL_REDIRECT = sbool(os.environ.get('SECURE_SSL_REDIRECT', 'false'))

if os.environ.get('CSRF_COOKIE_SECURE', None):
    CSRF_COOKIE_SECURE = sbool(os.environ.get('CSRF_COOKIE_SECURE', 'false'))

if os.environ.get('SECURE_HSTS_SECONDS', None):
    SECURE_HSTS_SECONDS = int(os.environ.get('SECURE_HSTS_SECONDS', 0))


# Crispy forms

CRISPY_TEMPLATE_PACK = os.environ.get('CRISPY_TEMPLATE_PACK', 'bootstrap4')
