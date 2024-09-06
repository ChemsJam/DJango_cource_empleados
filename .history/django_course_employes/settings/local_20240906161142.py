from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.msysql',
        'NAME': BASE_DIR / 'db.sqlite3',
        'database': "django_employes_course",
        'user': root,
        'password: = "Soyjohan123.",
        'default-character-set' = 'utf8',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'