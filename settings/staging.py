from base import *
import dj_database_url

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DATABASES['default'] = dj_database_url.config("CLEARDB_DATABASE_URL")

# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_lRJ210v4A3Z1wdwpi5469nZj')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_WQE2qg0XNQ0kqIOw8n0Ht0zu')

SITE_URL = ['http://127.0.0.1:8000', 'https://food-recipe-app.herokuapp.com/']
ALLOWED_HOSTS.append('food-recipe-app.herokuapp.com/')

# Log DEBUG information to the console
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}