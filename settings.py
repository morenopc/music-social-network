# -*- coding: utf-8 -*-
# Django settings for social pinax project.

import os.path
import posixpath
import pinax

PINAX_ROOT = os.path.abspath(os.path.dirname(pinax.__file__))
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
PROJECT_DIR = os.path.dirname(__file__)

# tells Pinax to use the default theme
PINAX_THEME = "default"

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# tells Pinax to serve media through the staticfiles app.
SERVE_MEDIA = DEBUG

INTERNAL_IPS = [
    "127.0.0.1",
]

ADMINS = [
    ("Moreno Cunha", "web.talentos@webtalentos.com.br"),
]

MANAGERS = ADMINS

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3", # Add "postgresql_psycopg2", "postgresql", "mysql", "sqlite3" or "oracle".
        "NAME": os.path.join(PROJECT_DIR, 'dev.db'),                       # Or path to database file if using sqlite3.
        "USER": "",                             # Not used with sqlite3.
        "PASSWORD": "",                         # Not used with sqlite3.
        "HOST": "",                             # Set to empty string for localhost. Not used with sqlite3.
        "PORT": "",                             # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Sao_Paulo'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'pt-br'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, "site_media", "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = "/site_media/media/"

# Absolute path to the directory that holds static files like app media.
# Example: "/home/media/media.lawrence.com/apps/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, "site_media", "static")

# URL that handles the static files like app media.
# Example: "http://media.lawrence.com"
STATIC_URL = "/site_media/static/"

# Additional directories which hold static files
STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, "media"),
    os.path.join(PINAX_ROOT, "media", PINAX_THEME),
]

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = posixpath.join(STATIC_URL, "admin/")

# Make this unique, and don't share it with anybody.
SECRET_KEY = "$mi$8_atv**bh+ma@w=b6dtjwekr#s5z=#+3b=_!olc6-5nah0"

DEFAULT_CHARSET = 'utf-8'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = [
    "django.template.loaders.filesystem.load_template_source",
    "django.template.loaders.app_directories.load_template_source",
]

MIDDLEWARE_CLASSES = [
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django_openid.consumer.SessionConsumer",
    "django.contrib.messages.middleware.MessageMiddleware",
    "groups.middleware.GroupAwareMiddleware",
    "pinax.apps.account.middleware.LocaleMiddleware",
    "django.middleware.doc.XViewMiddleware",
    "pagination.middleware.PaginationMiddleware",
    "django_sorting.middleware.SortingMiddleware",
    "pinax.middleware.security.HideSensistiveFieldsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = "dev.urls"

TEMPLATE_DIRS = [
    os.path.join(PROJECT_ROOT, "templates"),
    os.path.join(PINAX_ROOT, "templates", PINAX_THEME),
]

TEMPLATE_CONTEXT_PROCESSORS = [
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
    
    "staticfiles.context_processors.static_url",
    
    "pinax.core.context_processors.pinax_settings",
    
    "pinax.apps.account.context_processors.account",
    
    "notification.context_processors.notification",
    "announcements.context_processors.site_wide_announcements",
    "messages.context_processors.inbox",
    "friends_app.context_processors.invitations",
    
    "dev.context_processors.combined_inbox_count",
]

COMBINED_INBOX_COUNT_SOURCES = [
    "messages.context_processors.inbox",
    "friends_app.context_processors.invitations",
    "notification.context_processors.notification",
]

INSTALLED_APPS = [
    # Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.humanize",
    "django.contrib.markup",
    
    'django.contrib.comments',# Me
    
    "pinax.templatetags",
    
    # external
    "notification", # must be first
    "staticfiles",
    "debug_toolbar",
    "mailer",
    "uni_form",
    "django_openid",
    "ajax_validation",
    "timezones",
    "emailconfirmation",
    "announcements",
    "pagination",
    "friends",
    "messages",
    "oembed",
    "groups",
    "threadedcomments",
    "wakawaka",
    "swaps",
    "voting",
    "tagging",
    "bookmarks",
    "photologue",
    "avatar",
    "flag",
    "microblogging",
    "locations",
    "django_sorting",
    "django_markup",
    "tagging_ext",
    
    # Pinax
    "pinax.apps.account",
    "pinax.apps.signup_codes",
    "pinax.apps.analytics",
    "pinax.apps.profiles",
    "pinax.apps.blog",
    "pinax.apps.tribes",
    "pinax.apps.photos",
    "pinax.apps.topics",
    "pinax.apps.threadedcomments_extras",
    "pinax.apps.voting_extras",
    
    # project
    "about",
    # Me
    'perfis',
    'cadastro',
    'player',
    'colors',
    'homepage',
    'math_captcha',
    'ajaxcomments',
    'comentarios',
    'videos',
]

COMMENTS_APP = 'comentarios'
MATH_CAPTCHA_QUESTION = 'Qual o resultado?'

FIXTURE_DIRS = [
    os.path.join(PROJECT_ROOT, "fixtures"),
]

MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"

ABSOLUTE_URL_OVERRIDES = {
    "auth.user": lambda o: "/profiles/profile/%s/" % o.username,
}

MARKUP_FILTER_FALLBACK = "none"
MARKUP_CHOICES = [
    ("restructuredtext", u"reStructuredText"),
    ("textile", u"Textile"),
    ("markdown", u"Markdown"),
    ("creole", u"Creole"),
]

AUTH_PROFILE_MODULE = "profiles.Profile"
NOTIFICATION_LANGUAGE_MODULE = "account.Account"

ACCOUNT_OPEN_SIGNUP = True
ACCOUNT_REQUIRED_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = True
ACCOUNT_EMAIL_AUTHENTICATION = False # Me parece que ha um bug se True
ACCOUNT_UNIQUE_EMAIL = EMAIL_CONFIRMATION_UNIQUE_EMAIL = True

AUTHENTICATION_BACKENDS = [
    "pinax.apps.account.auth_backends.AuthenticationBackend",
    #'dev.apps.cadastro.auth_backends.CustomUserModelBackend',
]
#CUSTOM_USER_MODEL = 'cadastro.CustomUser'

CSRF_FAILURE_VIEW = 'csrf.csrf_failure'

LOGIN_URL = "/dev/account/login/" # @@@ any way this can be a url name?
LOGIN_REDIRECT_URLNAME = "home"

CONTACT_EMAIL = "sac@webtalentos.com.br"
SITE_NAME = "Web Talentos"

EMAIL_CONFIRMATION_DAYS = 2
EMAIL_DEBUG = DEBUG

DEFAULT_FROM_EMAIL = 'WebTalentos <sac@webtalentos.com.br>'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'sac@webtalentos.com.br'
EMAIL_HOST_PASSWORD = 'sac3talento7'
EMAIL_PORT = 587
EMAIL_SUBJECT_PREFIX = '[WebTalentos] '

ugettext = lambda s: s
LANGUAGES = [
#    ("en", u"English"),
     ('pt-br', u'Português'),
]

# URCHIN_ID = "ua-..."

YAHOO_MAPS_API_KEY = "..."

class NullStream(object):
    def write(*args, **kwargs):
        pass
    writeline = write
    writelines = write

RESTRUCTUREDTEXT_FILTER_SETTINGS = {
    "cloak_email_addresses": True,
    "file_insertion_enabled": False,
    "raw_enabled": False,
    "warning_stream": NullStream(),
    "strip_comments": True,
}

# if Django is running behind a proxy, we need to do things like use
# HTTP_X_FORWARDED_FOR instead of REMOTE_ADDR. This setting is used
# to inform apps of this fact
BEHIND_PROXY = False

FORCE_LOWERCASE_TAGS = True

# Uncomment this line after signing up for a Yahoo Maps API key at the
# following URL: https://developer.yahoo.com/wsregapp/
# YAHOO_MAPS_API_KEY = ""

DEBUG_TOOLBAR_CONFIG = {
    "INTERCEPT_REDIRECTS": False,
}

# local_settings.py can be used to override environment-specific settings
# like database and email that differ between development and production.
try:
    from local_settings import *
except ImportError:
    pass
