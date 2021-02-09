'''
This project doesn't actually use a config file.  this is just a test

@author: bjarm
'''

import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "maybethisisiftheenvironKeydoenstexist"
    REDIS_URL = "redis://:passwordtoREDIS@xxx.xxx.x.xxx:6379/0"