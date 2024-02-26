'''
Base settings applicable to all environments
'''

import environ
env = environ.Env()
# Reading .env file
environ.Env.read_env()

DEBUG = env.bool("DEBUG", default=False)
SECRET_KEY = env.str("SECRET_KEY")
DATABASES = {
    'default': env.db(),
}