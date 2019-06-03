import os
from .base import * #NOQA-->告诉PEP8规范工具，这个地方不需要检测


DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'multiplayer_blog',
        'USER':'root',
        'PASSWORD':'928587987',
        'HOST':'127.0.0.1',
        'PORT':3306,
        'OPTIONS':{'charset':'utf8mb4'}
    },
}

#INSTALLED_APPS += [
    #'debug_toolbar',
    #'pympler',
#]
#MIDDLEWARE += [
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
#]
DEBUG_TOOLBAR_CONFIG={
    'JQUERY_URL':'https://cdn.bootcss.com/jquery/3.3.1/jquery.min.js',
}
#INTERNAL_IPS=['127.0.0.1']

STATIC_ROOT = os.path.join(BASE_DIR, 'static_files/')


DEBUG_TOOLBAR_PANELS=[
    'pympler.panels.MemoryPanel',
]


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(levelname)s %(asctime)s %(module)s:'
                      '%(funcName)s:%(lineno)d %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'typeidea.log',
            'formatter': 'default',
            'maxBytes': 1024 * 1024,  # 1M
            'backupCount': 5,
        },

    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
    }
}
