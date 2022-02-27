from gym.settings.base import *
import environ

# Override base.py settings here
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR,'.env'))

DEBUG = True
SECRET_KEY = env('SECRET_KEY')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('DATABASE_NAME_DEV'),
        'USER':  env('DATABASE_USER'),
        'PASSWORD':  env('DATABASE_PASS'),
        'HOST': 'localhost',
        'PORT': 5432
    }
}