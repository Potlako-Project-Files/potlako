"""
Django settings for potlako project.

Generated by 'django-admin startproject' using Django 3.0.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import sys

import configparser
from django.conf.locale.en import formats as en_formats
from django.core.management.color import color_style

# from .logging import LOGGING
style = color_style()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

APP_NAME = 'potlako'
SITE_ID = 40

ETC_DIR = '/etc/'

LOGIN_REDIRECT_URL = 'home_url'

INDEX_PAGE = 'potlako-plus.bhp.org.bw:8000'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'o(^0$9zu2w5eby-^x&dd441d(@*#(+($can2uomfq%o(@p-fm+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', 'potlako-plus.bhp.org.bw',
                 'potlako-plus-dev.bhp.org.bw', '127.0.0.1']

CONFIG_FILE = f'{APP_NAME}.conf'

CONFIG_PATH = os.path.join(ETC_DIR, APP_NAME, CONFIG_FILE)
sys.stdout.write(style.SUCCESS(f'  * Reading config from {CONFIG_FILE}\n'))

config = configparser.RawConfigParser()
config.read(os.path.join(CONFIG_PATH))

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_crypto_fields.apps.AppConfig',
    'django_extensions',
    'simple_history',
    'corsheaders',
    'django_js_reverse',
    'rest_framework',
    'rest_framework.authtoken',
    'edc_action_item.apps.AppConfig',
    'edc_consent.apps.AppConfig',
    'edc_prn.apps.AppConfig',
    'edc_dashboard.apps.AppConfig',
    'edc_device.apps.AppConfig',
    'edc_lab.apps.AppConfig',
    'edc_locator.apps.AppConfig',
    'edc_reference.apps.AppConfig',
    'edc_metadata_rules.apps.AppConfig',
    'edc_model_admin.apps.AppConfig',
    'edc_navbar.apps.AppConfig',
    'edc_subject_dashboard.apps.AppConfig',
    'edc_label.apps.AppConfig',
    'edc_registration.apps.AppConfig',
    'edc_visit_schedule.apps.AppConfig',
    'edc_timepoint.apps.AppConfig',
    'potlako_dashboard.apps.AppConfig',
    'potlako_metadata_rules.apps.AppConfig',
    'potlako_reference.apps.AppConfig',
    'potlako_visit_schedule.apps.AppConfig',
    'potlako_prn.apps.AppConfig',
    'potlako_subject.apps.AppConfig',
    'potlako.apps.EdcDataManagerAppConfig',
    'potlako.apps.EdcAppointmentAppConfig',
    'potlako.apps.EdcMetadataAppConfig',
    'potlako.apps.EdcBaseAppConfig',
    'potlako.apps.EdcProtocolAppConfig',
    'potlako.apps.EdcVisitTrackingAppConfig',
    'potlako.apps.AppConfig',
    'potlako.apps.EdcFacilityAppConfig',
    'potlako.apps.EdcIdentifierAppConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'edc_dashboard.middleware.DashboardMiddleware',
    'edc_subject_dashboard.middleware.DashboardMiddleware',
    'edc_lab_dashboard.middleware.DashboardMiddleware'
]

ROOT_URLCONF = 'potlako.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'potlako.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': os.path.join(ETC_DIR, APP_NAME, 'mysql.conf'),
        },
    },
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {'NAME':
     'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
     },
    {'NAME':
     'django.contrib.auth.password_validation.MinimumLengthValidator',
     },
    {'NAME':
     'django.contrib.auth.password_validation.CommonPasswordValidator',
     },
    {'NAME':
     'django.contrib.auth.password_validation.NumericPasswordValidator',
     },
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

LANGUAGES = (
    ('tn', 'Setswana'),
    ('en', 'English'),
    ('kck', 'Ikalanga'),
)

DATE_INPUT_FORMATS = ['%d-%m-%Y']

TIME_ZONE = 'Africa/Gaborone'

USE_I18N = True

USE_L10N = False

USE_TZ = True

SITE_CODE = '40'
DEFAULT_STUDY_SITE = '40'
REVIEWER_SITE_ID = 41

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'potlako', 'static')

# dashboards
DASHBOARD_URL_NAMES = {
    'subject_listboard_url': 'potlako_dashboard:subject_listboard_url',
    'screening_listboard_url': 'potlako_dashboard:screening_listboard_url',
    'data_manager_listboard_url': 'edc_data_manager:data_manager_listboard_url',
    'subject_dashboard_url': 'potlako_dashboard:subject_dashboard_url',
}

LAB_DASHBOARD_URL_NAMES = {}

DASHBOARD_BASE_TEMPLATES = {
    'listboard_base_template': 'potlako/base.html',
    'dashboard_base_template': 'potlako/base.html',
    'data_manager_listboard_template': 'edc_data_manager/listboard.html',
    'screening_listboard_template': 'potlako_dashboard/screening/listboard.html',
    'subject_listboard_template': 'potlako_dashboard/subject/listboard.html',
    'subject_dashboard_template': 'potlako_dashboard/subject/dashboard.html',
}

CRISPY_TEMPLATE_PACK = 'bootstrap3'
GIT_DIR = BASE_DIR

EMAIL_BACKEND = config['email_conf'].get('email_backend')
EMAIL_HOST = config['email_conf'].get('email_host')
EMAIL_USE_TLS = config['email_conf'].get('email_use_tls')
EMAIL_PORT = config['email_conf'].get('email_port')
EMAIL_HOST_USER = config['email_conf'].get('email_user')
EMAIL_HOST_PASSWORD = config['email_conf'].get('email_host_pwd')

# edc_facility
HOLIDAY_FILE = os.path.join(BASE_DIR, 'holidays.csv')
COUNTRY = 'botswana'

PARENT_REFERENCE_MODEL1 = ''
PARENT_REFERENCE_MODEL2 = ''
