import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
from dotenv import load_dotenv
load_dotenv()

# Clave API de xAI
XAI_API_KEY = os.getenv("XAI_API_KEY")

SECRET_KEY = 'django-insecure--w(@_i5)pv&f)2yz_owdps&lmvn$7c9v=tu90dnag4^n2ua360'


DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'biblioaprende.juarez.gob.mx', '10.236.62.83', 'testbibliotecas.juarez.gob.mx', '10.236.62.44']



CSRF_TRUSTED_ORIGINS = [
    'https://biblioaprende.juarez.gob.mx',
    'https://testbibliotecas.juarez.gob.mx',
    'http://biblioaprende.juarez.gob.mx',  # Para pruebas
    'http://10.236.62.83',  # Para pruebas con IP
    'http://10.236.62.83:8085',
]

CSRF_COOKIE_SECURE = True  # Cambia a False si no usas HTTPS
SESSION_COOKIE_SECURE = True  # Cambia a False si no usas HTTPS

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# Logging para depuración
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'debug.log'),
        },
    },
    'loggers': {
        'django.security.csrf': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'crispy_tailwind',
    'rest_framework',
    'bibliotecarios',
    'bibliotecas',
    'fiadores',
    'libros',
    'registros',
    'users',
    'preregistro',
    'visita',
    'salas',
    'chatbot',
    'fichas',
    'prestamos',
    'estadisticas',
    'eventos',
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

ROOT_URLCONF = 'projects.urls'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'projects.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

AMBIENTE = 'PRUEBA_OLD'

BD_ALL = {
        'PRUEBA' : { 
            'default': {
                'ENGINE' : 'django.db.backends.postgresql',
                'NAME' : 'Biblios',
                'USER' : 'spif_user',
                'PASSWORD' : 'temporal',
                'HOST' : '10.236.62.44',
                'PORT' : '5434',
            }
        },
        'PRUEBA_OLD' : {
            'default': {
                'ENGINE' : 'django.db.backends.postgresql',
                'NAME' : 'Biblios',
                'USER' : 'postgres',
                'PASSWORD' : '123456',
                'HOST' : '10.236.62.93',
                'PORT' : '5433',
            }
        },
        'PRODUCCION' : {
            'default': {
                'ENGINE' : 'django.db.backends.postgresql',
                'NAME' : 'Biblios',
                'USER' : 'usr_biblios',
                'PASSWORD' : 'Ys3r.818lio5',
                'HOST' : '10.236.62.59',
                'PORT' : '5432',
            }
        }
    }

# DATABASES = BD_ALL[AMBIENTE]  if AMBIENTE in BD_ALL.keys() else BD_ALL['PRODUCCION']  --Jose
DATABASES = BD_ALL.get(AMBIENTE, BD_ALL['PRODUCCION'])
print(f"Base de datos configurada: {DATABASES}")



# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTH_USER_MODEL = 'registros.Registro'

# Configuración de sesiones
SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # Almacenamiento en base de datos (predeterminado)
SESSION_COOKIE_AGE = 86400  # Duración de la cookie en segundos (24 horas)
SESSION_EXPIRE_AT_BROWSER_CLOSE = False  # Mantener la sesión cuando se cierra el navegador
SESSION_SAVE_EVERY_REQUEST = True  # Guardar en cada petición, actualiza tiempo de expiración
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'  # Serializador para datos de sesión

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'es-mx'
TIME_ZONE = 'America/Mexico_City'
USE_TZ = True
USE_I18N = True
USE_L10N = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
  BASE_DIR / 'static',
]
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"

CRISPY_TEMPLATE_PACK = "tailwind"

LOGIN_REDIRECT_URL = 'index'
LOGOUT_REDIRECT_URL = 'index'
LOGIN_URL = "login"

DATA_UPLOAD_MAX_MEMORY_SIZE = 576716800  # 550 MB para permitir archivos grandes
FILE_UPLOAD_MAX_MEMORY_SIZE = 0  

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly"
    ]
}
