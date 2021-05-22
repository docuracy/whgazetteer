"""
Generated by 'django-admin startproject' using Django 2.0.7.

updates: 2.2.10 (20200211); 2.2.8(20191204); 2.2.4 (20190819); 2.1.7 (?); 2.1.2 (20181013)

"""

import os

# 
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/
# 

#
#DEBUG = True
#DEBUG = False

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.gis',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',

    # django-allauth 17 Feb 2021
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    #'allauth.socialaccount.providers.github',
    #'allauth.socialaccount.providers.google',
    #'allauth.socialaccount.providers.orcid',

    # 3rd party
    'bootstrap_modal_forms',
    'captcha',
    'django_celery_results',
    'django_extensions',
    'django_filters',
    'django_tables2',
    'djgeojson',
    'fontawesome',
    'guardian',
    'leaflet',
    'mathfilters',
    'rest_framework',
    'rest_framework_datatables',
    'rest_framework_gis',

    # project apps
    'accounts.apps.AccountsConfig',
    'api.apps.ApiConfig',
    'areas.apps.AreasConfig',
    # collections is reserved in python
    'collection.apps.CollectionConfig',
    'datasets.apps.DatasetsConfig',
    'main.apps.MainConfig',
    'maps.apps.MapsConfig',
    'places.apps.PlacesConfig',
    'search.apps.SearchConfig',
    'traces.apps.TracesConfig'
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',  
    'django.middleware.security.SecurityMiddleware',
]

ROOT_URLCONF = 'whg.urls'

PUBLIC_GROUP_ID = 'review'

TIME_ZONE = 'America/New_York'


CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'django-db'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = TIME_ZONE
# trying to throw error if no worker available
CELERY_TASK_EAGER_PROPAGATES = True

CAPTCHA_NOISE_FUNCTIONS = (
    #'captcha.helpers.noise_arcs',
    'captcha.helpers.noise_dots',)

# replacement section from drf-datatables
# https://django-rest-framework-datatables.readthedocs.io/en/latest/
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        #'api.views.PrettyJsonRenderer',
        #'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework_datatables.renderers.DatatablesRenderer',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework_datatables.filters.DatatablesFilterBackend',
        #'django_filters.rest_framework.DjangoFilterBackend'
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework_datatables.pagination.DatatablesPageNumberPagination',
    'PAGE_SIZE': 15000,
    #'PAGE_SIZE': 20,
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'main/templates'),
            os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': True,
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.debug',
                'django.template.context_processors.media',
                'django.template.context_processors.request',
            ],
            'builtins': [
                'whg.builtins',
            ]
        },
    },
]

WSGI_APPLICATION = 'whg.wsgi.application'


LEAFLET_CONFIG = {
    'TILES':[],
    'DEFAULT_CENTER': (35.0, 13.0),
    'DEFAULT_ZOOM': 1,
    'MIN_ZOOM': 1,
    'MAX_ZOOM': 14,
    'RESET_VIEW': False,
    #'MAX_BOUNDS_VISCOSITY': 0,
    'ATTRIBUTION_PREFIX': 
    "Tiles &copy; <a href='http://mapbox.com/' target='_blank'>MapBox</a> | "+
    "<a href='http://creativecommons.org/licenses/by-nc/3.0/deed.en_US' target='_blank'> CC-BY-NC 3.0</a>"
}

EMAIL_FILE_PATH = os.path.join(BASE_DIR, "sent_emails")

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL='/accounts/login/'
LOGOUT_REDIRECT_URL='/'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.postgresql',
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'whg',
        'USER':'',
        'PASSWORD':'',
        'HOST':'localhost',
        'PORT':'5432',
    }
}

# not implemented
# DATABASE_ROUTERS = ('whg.dbrouters.MyDBRouter',)

# /././././././.
# start django-allauth
# /././././././.
SITE_ID = 1 

ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS =1
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 86400 # 1 day in seconds

ACCOUNT_LOGOUT_REDIRECT_URL ='/'
LOGIN_REDIRECT_URL = '/accounts/email/' # default to /accounts/profile 

ACCOUNT_FORMS = {'signup': 'allauth.account.forms.WHGRegisterForm',}

#URL_FRONT = 'http://localhost:8000/'
URL_FRONT = 'http://whgazetteer.org/'

#SOCIALACCOUNT_PROVIDERS = {
    ## For each OAuth based provider, either add a ``SocialApp``
    ## (``socialaccount`` app) containing the required client
    ## credentials, or list them here:
    #'github': {
        #'APP': {
            #'client_id': '123',
            #'secret': '456',
            #'key': ''
        #}
    #},
    #'orcid': {
            ## Base domain of the API. Default value: 'orcid.org', for the production API
            #'BASE_DOMAIN':'sandbox.orcid.org',  # for the sandbox API
            ## Member API or Public API? Default: False (for the public API)
            #'MEMBER_API': True,  # for the member API
    #}}
# /././././././.
# end django-allauth
# /././././././.

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend', # default
    'guardian.backends.ObjectPermissionBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'whg/static/'),
    os.path.join(BASE_DIR, 'datasets/static/'),
]

try:
    from .local_settings import *
except ImportError:
    pass