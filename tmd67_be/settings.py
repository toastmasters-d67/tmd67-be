"""
Django settings for tmd67_be project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = (
    "django-insecure-a+lqh%d(^o9srdd8zsn9kqgvw6#mpw08a74vi3ek&jnx-$(!tr"
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "django_filters",
    "tmd67_be.api",
    "tmd67_be.ac",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "tmd67_be.urls"

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

WSGI_APPLICATION = "tmd67_be.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME") or "postgres",
        "USER": os.getenv("USER_NAME") or "tmdadm",
        "PASSWORD": os.getenv("PASSWORD") or "tmd+123",
        "HOST": os.getenv("HOST_NAME") or "127.0.0.1",
        "PORT": os.getenv("PORT") or "5432",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = "static"
MEDIA_URL = "media/"
MEDIA_ROOT = "media"
LOGOUT_REDIRECT_URL = "/"
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend"
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
}

STRAWBERRY_DJANGO = {
    "FIELD_DESCRIPTION_FROM_HELP_TEXT": True,
    "TYPE_DESCRIPTION_FROM_MODEL_DOCSTRING": True,
}

if "WEBSITE_HOSTNAME" in os.environ:  # Running on Azure
    from .azure import *  # disable --remove-all-unused-imports


OAUTH2 = {
    "Google": {
        "auth_uri": "https://accounts.google.com/o/oauth2/v2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "client_id": os.environ.get(
            "GG_CLIENT_ID",
            "199688192618-d0fflt4qitm34of553ecr60fpbfmoirt.apps.googleusercontent.com",
        ),
        "client_secret": os.environ.get(
            "GG_CLIENT_SECRET", "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"
        ),
        "redirect_uri": os.environ.get(
            "GG_REDIRECT_URI",
            "https://testtmd67api.azurewebsites.net/google/callback/",
        ),
        "scope": ["openid", "profile", "email"],
    }
}


NEWEB_PAY = {
    "MerchantID": os.environ.get("MerchantID", "MS147585948"),
    "HashKey": os.environ.get("HashKey", "CJ2veMaN9yTOZ1f90lN3SVPHEinSloU5"),
    "HashIV": os.environ.get("HashIV", "C0omfPbq8R2epI1P"),
    "Version": os.environ.get("Version", "1.5"),
    "MPG_GW": os.environ.get(
        "MPG_GW", "https://ccore.newebpay.com/MPG/mpg_gateway"
    ),
    "NotifyURL": os.environ.get(
        "NOTIFY_URL",
        "https://testtmd67api.azurewebsites.net/payment-records/neweb-pay-notify",
    ),
    "ReturnURL": os.environ.get(
        "RETURN_URL",
        "https://testtmd67api.azurewebsites.net/payment-records/neweb-pay-return",
    ),
}
