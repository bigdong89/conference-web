"""
Django settings for foo project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# A list of all the people who get code error notifications.
ADMINS = (
    ('Ivan Habunek', 'ivan@habunek.com'),
    ('WebCamp', 'info@webcampzg.org')
)

MANAGERS = ADMINS


def ABS_PATH(*args):
    return os.path.abspath(os.path.join(BASE_DIR, *args))


def ensure_secret_key_file():
    """Checks that secret.py exists in settings dir. If not, creates one
    with a random generated SECRET_KEY setting."""
    secret_path = os.path.join(ABS_PATH('settings'), 'secret.py')
    if not os.path.exists(secret_path):
        from django.utils.crypto import get_random_string
        secret_key = get_random_string(50, 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)')
        with open(secret_path, 'w') as f:
            f.write("SECRET_KEY = " + repr(secret_key) + "\n")


ensure_secret_key_file()
from .secret import SECRET_KEY  # noqa

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.flatpages',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'django.contrib.staticfiles',

    'raven.contrib.django.raven_compat',
    'tinymce',
    'markdown_deux',

    'ui',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'blog',
    'cfp',
    'config',
    'dashboard',
    'events',
    'jobs',
    'pages',
    'people',
    'schedule',
    'sponsors',
    'talks',
    'usergroups',
    'voting',
)


MIDDLEWARE = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'pages.middleware.PageFallbackMiddleware',
)

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",

    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)

# The model to use to represent a User.
# https://docs.djangoproject.com/en/1.11/ref/settings/#std:setting-AUTH_USER_MODEL
AUTH_USER_MODEL = 'people.User'

ROOT_URLCONF = 'project.urls'

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config()
}

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Zagreb'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

# URL to use when referring to static files located in STATIC_ROOT.
STATIC_URL = '/static/'

# Additional locations the staticfiles app will traverse.
STATICFILES_DIRS = [
    ABS_PATH('../ui/dist'),
]

# The absolute path to the directory where collectstatic will collect static files for deployment.
STATIC_ROOT = ABS_PATH('static')


# Media (user uploaded) files
# https://docs.djangoproject.com/en/1.11/topics/files/

MEDIA_ROOT = os.getenv('MEDIA_ROOT', ABS_PATH('media'))

MEDIA_URL = '/media/'

# Settings for django.contrib.sites.
# https://docs.djangoproject.com/en/1.11/ref/settings/#id17
SITE_ID = 1

# Sending emails
# https://docs.djangoproject.com/en/1.11/topics/email/
EMAIL_USE_TLS = True
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_USER = os.getenv('EMAIL_USER')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
EMAIL_PORT = os.getenv('EMAIL_PORT')

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Settings for django-allauth
# http://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_SIGNUP_FORM_CLASS = 'ui.forms.SignupForm'
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

# Logging
# https://docs.djangoproject.com/en/1.11/topics/logging/
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


TINYMCE_DEFAULT_CONFIG = {
    'theme': "advanced",
    'theme_advanced_toolbar_location': "top",
    'theme_advanced_resizing': True,
    'plugins': 'table,contextmenu,paste,autoresize,media,lists,style',
    'paste_text_sticky': True,
    'paste_text_sticky_default': True,
    'paste_retain_style_properties': 'font-weight,font-style',  # preserve bold and italic text
    'paste_remove_styles': True,
    'paste_remove_styles_if_webkit': True,
    'paste_text_linebreaktype': 'p',
    'paste_remove_spans': True,
    'paste_strip_class_attributes': True,
    'content_css': STATIC_URL + 'admin/tinymce.css',
    'theme_advanced_buttons1': str("style,bold,italic,underline,separator,"
        "bullist,separator,separator,undo,redo,image,link"),
    'theme_advanced_buttons2': "cleanup,lists,pasteword,table,contextmenu,media,code",
    'theme_advanced_buttons3': "",
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Default
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # Additional
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',

                # Custom
                'ui.ctx.event',
                'ui.ctx.navigation',
                'ui.ctx.sponsors',
                'ui.ctx.team',
                'ui.ctx.usergroups',
                'ui.ctx.webcamp',
            ],
            'string_if_invalid': '<< MISSING VARIABLE "%s" >>' if DEBUG else '',
        },
    },
]

# Markdown deux settings
# https://github.com/trentm/django-markdown-deux#settings
MARKDOWN_DEUX_STYLES = {
    "default": {
        "extras": {
            "tables": None,
            "code-friendly": None,
        },
        "safe_mode": "escape",
    },
    # A trusted style which doesn't escape html
    "trusted": {
        "extras": {
            "tables": None,
            "code-friendly": None,
        },
        "safe_mode": False,
    }
}

#
# WebCamp custom settings
#

# Set to false to disallow changing talk contents
ALLOW_TALK_UPDATES = True

TICKET_HOLDER_GROUP_NAME = 'TicketHolders'
TALK_COMMITTEE_GROUP_NAME = 'TalkCommittee'

VOTING_ENABLED = False
