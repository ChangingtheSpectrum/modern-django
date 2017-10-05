from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY', default="""r)h^-3m(=w!h@o7v(za=+6nwt4zst_86_#6m8@rs=^@ada+d(x'""")

DEBUG = env.bool('DJANGO_DEBUG', True)