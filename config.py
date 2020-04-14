import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = 'be2cd0c96bb0766dda6ea3f74f2cd3ed902e78ef45ba5908526202a4c7759727'
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')

