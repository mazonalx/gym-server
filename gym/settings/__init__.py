from .base import *
import environ
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR,'.env'))

if env('ENV_NAME') == 'Production':
    try:
        from .prod import *
    except:
        pass
elif env('ENV_NAME') == 'Staging':
    try:
        from .staging import *
    except:
        pass
else:
    try:
        from .local import *
    except:
        pass