"""
Django settings for caspraypros project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
project_name = 'webdesign'
site_url = '.zparkweb.com'
SITE_ID = 1

import django.conf.global_settings as DEFAULT_SETTINGS

THIRD_PARTY_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'sekizai.context_processors.sekizai',
    'cms.context_processors.cms_settings',
    'django_facebook.context_processors.facebook',
)

LOCAL_CONTEXT_PROCESSORS = (
    "context_processors.site_settings_processor",
)

TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + THIRD_PARTY_CONTEXT_PROCESSORS + LOCAL_CONTEXT_PROCESSORS

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
gettext = lambda s: s
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_PATH = os.path.join(BASE_DIR, 'static')
STATIC_ROOT = os.path.join(BASE_DIR, 'local_static')
STATICFILES_DIRS = (
    STATIC_PATH,
    )

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
IS_PRODUCTION = os.environ.get('IS_PRODUCTION')
if IS_PRODUCTION is None:
    IS_PRODUCTION = False
elif IS_PRODUCTION == 'True':
    IS_PRODUCTION = True

if IS_PRODUCTION:
    DEBUG = False
else:
    DEBUG = True

TEMPLATE_DEBUG = False

AUTH_PROFILE_MODULE = 'myProfiles.UserProfile'

AUTHENTICATION_BACKENDS = (
    'django_facebook.auth_backends.FacebookBackend',
    'django.contrib.auth.backends.ModelBackend',
)

ALLOWED_HOSTS = [
    site_url,
]

TEMPLATE_DIRS = [
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    TEMPLATE_PATH,
]

#django-cms req's
CMS_TEMPLATES = (
    ('cms/template_1.html', gettext('Template One')),
    ('cms/index.html', gettext('Index')),
    ('cms/base_sidebar_left.html', gettext('Base Sidebar L')),
    ('cms/base_sidebar_both.html', gettext('Base Sidebar L+R')),
    ('cms/base_sidebar_left_pills.html', gettext('Base Sidebar L Pills')),
)

CMS_PLACEHOLDER_CONF = {
    'main_image': {
        'plugins': ['FilerImagePlugin'],
    },
    'main_image_2': {
        'plugins': ['FilerImagePlugin'],
    },
    'main_image_text': {
        'plugins': ['TextPlugin'],
    },
    'content_top_text': {
        'plugins': ['TextPlugin'],
    },
}

CMS_SEO_FIELDS = True

# Application definition
DEFAULT_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'south',
    'registration',
    'crispy_forms',
    'reversion',
    'djangocms_text_ckeditor', #text editor for cms 3+
    'cms',  # django CMS itself
    'mptt',  # utilities for implementing a tree
    'menus',  # helper for model independent hierarchical website navigation
    'sekizai',  # for javascript and css management
    'djangocms_admin_style',  # for the admin skin. You **must** add 'djangocms_admin_style' in the list **before** 'django.contrib.admin'.
    'filer',
    'easy_thumbnails',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_link',
    'cmsplugin_filer_image',
    'cmsplugin_filer_teaser',
    'cmsplugin_filer_video',
    'polls',
    'django_facebook',
)

CKEDITOR_SETTINGS = {
    'autoParagraph': False
}

THUMBNAIL_HIGH_RESOLUTION = True

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

LOCAL_APPS = (
    'myProfiles',
    'myQuotes',
    'homepage',
    'contact',
)

INSTALLED_APPS = THIRD_PARTY_APPS + LOCAL_APPS + DEFAULT_APPS

FACEBOOK_APP_ID = os.environ.get('FACEBOOK_APP_ID')
FACEBOOK_APP_SECRET = os.environ.get('FACEBOOK_APP_SECRET')

REGISTRATION_OPEN = True
ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_AUTO_LOGIN = True
LOGIN_REDIRECT_URL = '/profiles/home/'
LOGIN_URL = '/accounts/login/'

ROOT_URLCONF = project_name +'.urls'

WSGI_APPLICATION = project_name + '.wsgi.application'

# EMAIL SETTTINGS
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = 'jaredjamespark@gmail.com'
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'jaredjamespark@gmail.com'
SERVER_EMAIL = 'jaredjamespark@gmail.com'

CRISPY_TEMPLATE_PACK = 'bootstrap3'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
)

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'
LANGUAGES = [
    ('en-us', 'English'),
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

if not IS_PRODUCTION:
    from settings_dev import *
