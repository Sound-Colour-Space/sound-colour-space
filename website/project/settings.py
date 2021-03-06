import os
import sys

from django.utils.translation import ugettext_lazy as _

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))

sys.path.insert(0, os.path.join(BASE_DIR, "apps"))
sys.path.insert(0, os.path.join(BASE_DIR, "common"))

ALLOWED_HOSTS = ['*', ]
SITE_ID = 1

INSTALLED_APPS = (
    'admin_tools',
    # 'admin_tools.theming',
    # 'admin_tools.menu',
    'admin_tools.dashboard',
    'django_slick_admin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'gunicorn',
    'django_extensions',
    'compressor',
    'sekizai',
    'celery_haystack',
    'easy_thumbnails',
    'tastypie',
    'adminsortable2',
    'haystack',
    'taggit',
    'accounts',
    'museum'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.request',
                # sekizai
                'sekizai.context_processors.sekizai',
                # api and base url
                'common.context_processors.api_url',
                'common.context_processors.base_url',
                'common.context_processors.media_url',
                'common.context_processors.diagrams_url',
            ],
            'loaders': [
                # admin tools
                'admin_tools.template_loaders.Loader',
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader'
            ]
        },
    },
]

APPEND_SLASH = True

'''
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin
    'django.contrib.auth.backends.ModelBackend',
)
'''

ROOT_URLCONF = 'project.urls'
WSGI_APPLICATION = 'project.wsgi.application'

LANGUAGES = [
    ('en', _('English')),
    #('de', _('German')),
]

# i18n
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Zurich'
USE_I18N = True
USE_L10N = True
#USE_TZ = True
USE_TZ = False

# static configuration
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # django compressor
    'compressor.finders.CompressorFinder',
)
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'site-static'),
)
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
DIAGRAMS_ROOT = os.path.join(BASE_DIR, 'media/diagrams')
DIAGRAMS_URL = '/media/diagrams/'
EXPERIMENTS_ROOT = os.path.join(BASE_DIR, 'media/experiments')
EXPERIMENTS_URL = '/media/experiments/'
EXHIBITIONS_ROOT = os.path.join(BASE_DIR, 'media/exhibitions')
EXHIBITIONS_URL = '/media/exhibitions/'

# easy_thumbnails
THUMBNAIL_QUALITY = 95
THUMBNAIL_PRESERVE_EXTENSIONS = True
THUMBNAIL_MEDIA_ROOT = os.path.join(DIAGRAMS_ROOT, 'thumbs')
THUMBNAIL_MEDIA_URL = DIAGRAMS_URL + 'thumbs/'

THUMBNAIL_ALIASES = {
    'museum.Entry.image': {
        'x-small': {
            'quality': 95,
            'size': (271, 0),
        },
        'small': {
            'quality': 95,
            'size': (400, 0),
        },
        'medium': {
            'quality': 95,
            'size': (554, 0),
        },
        'large': {
            'quality': 95,
            'size': (1108, 0),
        },
    },
}

# tastypie
API_VERSION = 'v1'
API_URL = '/api/' + API_VERSION + '/'
TASTYPIE_ALLOW_MISSING_SLASH = True

# user model
AUTH_USER_MODEL = 'accounts.MyUser'

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login'
LOGOUT_URL = '/logout'

# haystack
HAYSTACK_DOCUMENT_FIELD = 'fulltext'
#HAYSTACK_DEFAULT_OPERATOR = 'OR'
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'haystack',
    },
}
# auto update search index
#HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
HAYSTACK_SIGNAL_PROCESSOR = 'celery_haystack.signals.CelerySignalProcessor'

# load local_settings
try:
    from local_settings import *
except ImportError:
    pass
