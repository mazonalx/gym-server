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
        #'ENGINE': 'django.db.backends.sqlite3',
        'NAME': env('DATABASE_NAME_DEV'),
        #'NAME': 'gym_dev',
        'USER':  env('DATABASE_USER'),
        #'USER':  'proxyalx',
        'PASSWORD':  env('DATABASE_PASS'),
        #'PASSWORD':  'proxyalx',
        'HOST': 'localhost',
        'PORT': 5432
    }
}