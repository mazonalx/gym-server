from gym.settings.base import *
import environ

# Override base.py settings here
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR,'.env'))

DEBUG = False
SECRET_KEY = env('SECRET_KEY')
ALLOWED_HOSTS = ['localhost','127.0.0.1']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('DATABASE_NAME_PROD'),
        'USER':  env('DATABASE_USER'),
        'PASSWORD':  env('DATABASE_PASS'),
        'HOST': 'localhost',
        'PORT': 5432
    }
}