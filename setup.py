#!/usr/bin/env python

from setuptools import setup, find_packages
#from cabot.cabotapp.alert import AlertPlugin
from cabot.cabotapp.alert import AlertPluginUserData
from django.db import models
#from cabot.cabotapp.alert import AlertPluginUserData

setup(name='cabot-alert-skeleton',
      version='1.0.0',
      description='A skeleton plugin for Cabot by Arachnys',
      author='Manoj',
      author_email='manoj.palavalasa@mycroft.ai',
      url='http://cabotapp.com',
      packages=find_packages(),
      download_url = 'https://github.com/cabotapp/cabot-alert-skeleton/tarball/1.0.0',
     )
