import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

SECRET_KEY = 'django-insecure-n5@fl3@=^vx&f8qk2nd=1xabs=7rw*+lg^3-$o0hq=f$6(4zjn'

# DEBUG = False
DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'user.apps.UserConfig',
    'student.apps.StudentConfig',
    'teacher.apps.TeacherConfig',
    'department.apps.DepartmentConfig',
    'college.apps.CollegeConfig',
    'gallery.apps.GalleryConfig',
    'exam.apps.ExamConfig',
    'staff.apps.StaffConfig',
    'django_extensions',
    'crispy_forms',
    'import_export',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'college.context_processors.extras'
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': 'college',
       'USER': 'postgres',
       'PASSWORD': '123456',
       'HOST': 'localhost',
       'PORT': '5432',
   }
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'user.User'
CRISPY_TEMPLATE_PACK = 'bootstrap4'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# STATIC_ROOT = os.path.join(BASE_DIR, 'static') ->
# STATICFILES_DIRS setting should not contain the STATIC_ROOT
MEDIA_URL = ''
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

# celery config
# CELERY_BROKER_URL = 'redis://127.0.0.1:6379'

# CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379'
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'
# CELERY_ACCEPT_CONTENT = ['application/json']
#
# CELERY_BROKER_URL = 'amqp://guest:guest@localhost'
# CELERY_ACCEPT_CONTENT = ['json']
# CELERY_RESULT_BACKEND = 'db+sqlite:///results.sqlite'
# CELERY_TASK_SERIALIZER = 'json'
