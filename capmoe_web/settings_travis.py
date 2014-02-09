# -*- coding: utf-8 -*-
"""
    :synopsis: Some setting variables are overridden here for travis ci.
"""


# standard modules

# 3rd party modules

# original modules
from capmoe_web.settings import *


DEBUG = False

TEMPLATE_DEBUG = False

DATABASES = {
    'default': {
        'ENGINE'   : 'django.db.backends.mysql',
        'NAME'     : 'capmoe_travis',
        'USER'     : 'travis',
        'PASSWORD' : '',
        'HOST'     : '127.0.0.1',
    }
}
