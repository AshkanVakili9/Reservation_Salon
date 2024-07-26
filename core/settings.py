from datetime import timedelta
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = "django-insecure-7l3xdm0oouw0vzhg49ql^khpe*2u@0t(n=e^(u2%&e4nz^!4qh"


DEBUG = True

ALLOWED_HOSTS = ['*']


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    
    "rest_framework_simplejwt",
    "rest_framework",
    "requests",
    "iranian_cities",
    'azbankgateways',
    
    "user.apps.UserConfig",
    "salon.apps.SalonConfig",
]

AUTH_USER_MODEL = "user.User"

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
}

SIMPLE_JWT = {
    "TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.MyTokenObtainPairSerializer",
    "ACCESS_TOKEN_LIFETIME": timedelta(days=30),
}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite",
    }
}


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',       
#     }
# }


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = 'fa-ir'

TIME_ZONE = 'Asia/Tehran'

# LANGUAGE_CODE = "en-us"

# TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
# # MEDIA_ROOT = os.path.join(BASE_DIR, "
# STATIC_URL = "static/"
# MEDIA_URL = "images/"

# STATICFILES_DIRS = [BASE_DIR]

# MEDIA_ROOT = "static/images"



# ...

# Change the location where Django will collect and create static files.
# Here, we're specifying the "staticfiles" directory within your BASE_DIR.
# STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# STATIC_URL = "/static/"
# MEDIA_URL = "/images/"

# # Specify the location where Django should look for additional static files.
# STATICFILES_DIRS = [os.path.join(BASE_DIR, "staticfiles/static")]

# # Specify the root location where uploaded media files should be stored.
# MEDIA_ROOT = os.path.join(BASE_DIR, "staticfiles/static/images")


MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/media')

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/static')






DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]


AZ_IRANIAN_BANK_GATEWAYS = {
   'GATEWAYS': {
       'IDPAY': {
           'MERCHANT_CODE': '<YOUR MERCHANT CODE>',
           'METHOD': 'POST',  # GET or POST
           'X_SANDBOX': 1,  # 0 disable, 1 active
       },
       
   },
   'IS_SAMPLE_FORM_ENABLE': True, # اختیاری و پیش فرض غیر فعال است
   'DEFAULT': 'IDPAY',
   'CURRENCY': 'IRR', # اختیاری
   'TRACKING_CODE_QUERY_PARAM': 'tc', # اختیاری
   'TRACKING_CODE_LENGTH': 16, # اختیاری
   'SETTING_VALUE_READER_CLASS': 'azbankgateways.readers.DefaultReader', # اختیاری
   'BANK_PRIORITIES': [
   ], # اختیاری
   'IS_SAFE_GET_GATEWAY_PAYMENT': True, #اختیاری، بهتر است True بزارید.
   'CUSTOM_APP': None, # اختیاری 
}
