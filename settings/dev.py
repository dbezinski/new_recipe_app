from base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_lRJ210v4A3Z1wdwpi5469nZj')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_WQE2qg0XNQ0kqIOw8n0Ht0zu')

STATIC_URL = 'http://127.0.0.1:8000/recipe_app/'
SITE_URL = ['http://127.0.0.1:8000', 'http://food-recipe-app.herokuapp.com/']