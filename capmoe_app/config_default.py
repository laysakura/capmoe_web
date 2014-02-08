# -*- coding: utf-8 -*-
"""
    capmoe_app.config_default
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    :synopsis: Default configs for CapMoe web server

    Override these default values in your `config.py`
"""


# standard modules
from os.path import join
from tempfile import gettempdir

# 3rd party modules

# original modules


config = {
    'img_dir'    : join(gettempdir(), 'CapMoeImg'),
    'thumb_dir'  : join(gettempdir(), 'CapMoeThumb'),
    'img_suffix' : 'jpg',
}
