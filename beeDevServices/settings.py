from pathlib import Path
import os
from environ import Env

env = Env()
env.read_env()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'KEY'

DEBUG = True
# DEBUG = False

ALLOWED_HOSTS = []
# ALLOWED_HOSTS = ['beedev-services.com', 'dev.beedev-services.com'']

CORS_ALLOWED_ORIGINS = [
    'http://127.0.0.1:8000',
    'http://127.0.0.1:5500',
    'http://localhost:5173',
    'https://beedev-services.com',
    'http://beedev-services.com',
    'https://dev.beedev-services.com',
    'http://dev.beedev-services.com',
]
CORS_ALLOWED_ALL_ORIGINS: True


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'coreApp.apps.CoreappConfig',
    'adminApp.apps.AdminappConfig',
    'customerApp.apps.CustomerappConfig',
    'orderApp.apps.OrderappConfig',
    'corsheaders',
    'rest_framework',
    # 'django_hosts',
]

MIDDLEWARE = [
    # 'django_hosts.middleware.HostsRequestMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django_hosts.middleware.HostsResponseMiddleware'
]

ROOT_URLCONF = 'beeDevServices.urls'
# ROOT_HOSTCONF = 'beeDevServices.hosts'
# DEFAULT_HOST= 'www'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'beeDevServices.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR,'db.sqlite3'),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'mysql.connector.django',
#         # 'ENGINE':'django.db.backends.mysql',
#         'NAME': 'thehives_beedev',
#         'USER': 'root',
#         # 'USER': 'thehives_services',
#         'PASSWORD': 'HoneyBee#4',
#         # 'PASSWORD': 'MrTucker@22',
#         'HOST': 'localhost',
#         'PORT': '3306',
#         # 'OPTIONS': {'charset': 'utf8mb4'},
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'US/Eastern'

USE_I18N = True

USE_TZ = True


STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = 'static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
# EMAIL_PORT = 465
# EMAIL_HOST_USER = 'beedev.services@gmail.com'
EMAIL_HOST_PASSWORD = 'HOST_PASSWORD'
EMAIL_HOST_ALT_USER = 'melissa@beedev-services.com'
