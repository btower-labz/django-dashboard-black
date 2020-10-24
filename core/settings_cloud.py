# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

import os
from decouple import config
from unipath import Path
import dj_database_url
import boto3
from .ssm_parameter_store import SSMParameterStore
import json

# AWS Secrets Manager Client
secrets = boto3.client("secretsmanager")

# AWS Parameters Store Client
#ssm_client = boto3.client('ssm')
#parameter = ssm.get_parameter(Name='/Prod/Db/Password', WithDecryption=True)
store = SSMParameterStore(prefix=config('DJANGO_SETTINGS_PREFIX', default='/dev'), ttl=60)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = store['DJANGO_SECRET']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False)

ALLOWED_HOSTS = ['*','localhost', '127.0.0.1', config('SERVER', default='127.0.0.1')]

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASE_SECRET_ARN = store['DATABASE_SECRET_ARN']
DATABASE_SECRET_VALUE = json.loads(secrets.get_secret_value(SecretId=DATABASE_SECRET_ARN)['SecretString'])

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': store['DATABASE_NAME'],
        'USER': DATABASE_SECRET_VALUE['username'],
        'PASSWORD': DATABASE_SECRET_VALUE['password'],
        'HOST': store['DATABASE_HOST'],
        'PORT': store['DATABASE_PORT'],
        #'OPTIONS': {
        #    'read_default_file': '/path/to/my.cnf',
        #},
    }
}
