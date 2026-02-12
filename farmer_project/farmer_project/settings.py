from pathlib import Path
import os
from django.utils.translation import gettext_lazy as _
import dj_database_url

# --------------------------------------------------
# BASE DIRECTORY
# --------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent


# --------------------------------------------------
# SECURITY SETTINGS
# --------------------------------------------------
SECRET_KEY = 'django-insecure-change-this-key-later'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
ALLOWED_HOSTS = ['*']

# --------------------------------------------------
# API KEYS
# --------------------------------------------------
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

FAST2SMS_API_KEY = "QHP0sYmjnK51VJEtU68XxADbuc3oedOfazIiG7RgBMTwZNCW4pfD9HXxSBpWvdreNFm2jYchPL0znast"


# --------------------------------------------------
# APPLICATION DEFINITION
# --------------------------------------------------
INSTALLED_APPS = [
    'core',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]


# --------------------------------------------------
# MIDDLEWARE  ✅ LANGUAGE SUPPORT ENABLED
# --------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    # ✅ REQUIRED FOR LANGUAGE SWITCH
    'django.middleware.locale.LocaleMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# --------------------------------------------------
# URL CONFIG
# --------------------------------------------------
ROOT_URLCONF = 'farmer_project.urls'


# --------------------------------------------------
# TEMPLATES CONFIG
# --------------------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # global templates folder
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# --------------------------------------------------
# WSGI
# --------------------------------------------------
WSGI_APPLICATION = 'farmer_project.wsgi.application'


# --------------------------------------------------
# DATABASE
# --------------------------------------------------
DATABASES = {
    'default': dj_database_url.parse(
        "postgresql://postgres:dbUfUJoxrXOkZtSdxOjFbIwhhaJwPsvI@ballast.proxy.rlwy.net:58438/railway"
    )
}

# --------------------------------------------------
# PASSWORD VALIDATION
# --------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# --------------------------------------------------
# LANGUAGE & INTERNATIONALIZATION  🌐
# --------------------------------------------------
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGE_CODE = 'en'

LANGUAGES = [
    ('en', _('English')),
    ('hi', _('Hindi')),
    ('te', _('Telugu')),
    ('ta', _('Tamil')),
    ('kn', _('Kannada')),
    ('ml', _('Malayalam')),
    ('mr', _('Marathi')),
    ('bn', _('Bengali')),
    ('gu', _('Gujarati')),
    ('pa', _('Punjabi')),
    ('or', _('Odia')),
    ('as', _('Assamese')),
    ('ur', _('Urdu')),
]

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

TIME_ZONE = 'Asia/Kolkata'


# --------------------------------------------------
# STATIC FILES
# --------------------------------------------------
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]


# --------------------------------------------------
# MEDIA FILES  ✅ REQUIRED FOR IMAGE UPLOADS
# --------------------------------------------------
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# --------------------------------------------------
# DEFAULT PRIMARY KEY
# --------------------------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# --------------------------------------------------
# AUTH SETTINGS
# --------------------------------------------------
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/dashboard/'
LOGOUT_REDIRECT_URL = '/login/'


# --------------------------------------------------
# SESSION (LANGUAGE PERSISTENCE)
# --------------------------------------------------
LANGUAGE_COOKIE_NAME = 'django_language'
LANGUAGE_COOKIE_AGE = 60 * 60 * 24 * 365  # 1 year


# ADMIN EMAIL (HIDDEN)
ADMIN_EMAIL = "valasareddymohith@gmail.com"


