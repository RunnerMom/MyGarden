# Config
# -*- coding: utf-8 -*-

import os

from signal import signal, SIGPIPE, SIG_DFL 
#Ignore SIG_PIPE and don't throw exceptions on it... (http://docs.python.org/library/signal.html)
signal(SIGPIPE,SIG_DFL) 

#Flask secret key
SECRET_KEY = os.environ.get('key')

#Linkedin secret key
CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")
api_key = os.environ.get("api_key")

WTF_CSRF_ENABLED = True
WTF_CSRF_SECRET_KEY = os.environ.get('key') 

LINKEDIN_API_KEY = os.environ.get('linkedin_api')

basedir = os.path.abspath(os.path.dirname(__file__))

# Code to setup a postgres database
if os.environ.get('DATABASE_URL') is None:
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/developher2'
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

# Stores migrate data files
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'sunfinder_db_repository')

# Threashold for slow loading (in seconds)
DATABASE_QUERY_TIMEOUT = 0.5

