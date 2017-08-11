SECRET_KEY = 'la-la-la'

INSTALLED_APPS = [
    'django_extensions',
    'django_coreapi_client',
]

MIDDLEWARE = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    }
}

COREAPI_CLIENT = {
    'example_server': {
        'SCHEMA_URL': 'https://example.com/api/schema/',
        'AUTH_USERNAME': 'client-example',
        'AUTH_PASSWORD': 'password-example',
    },
}
