from .default import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sis_python',
        'USER': 'sisqualis',
        'PASSWORD': 'sisqualis',
        'HOST': 'localhost',
    }
}