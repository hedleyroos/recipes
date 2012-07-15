from recipes.settings import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'recipes_qa',
        'USER': 'recipes_qa',
        'PASSWORD': 'recipes_qa',
        'HOST': '',
        'PORT': '',
    }
}

MEDIA_ROOT = '%s/../media-qa/' % BUILDOUT_PATH

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'KEY_PREFIX': 'recipes_qa',
    }
}

CKEDITOR_UPLOAD_PATH = '%s/../media-qa/uploads/' % BUILDOUT_PATH
