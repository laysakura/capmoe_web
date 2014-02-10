# -*- coding: utf-8 -*-
"""
    capmoe_app.config_default
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    :synopsis: Default configs for CapMoe web server

    Override these default values in your `config.py`
"""

# python 2.x support
from __future__ import division, print_function, absolute_import, unicode_literals

# standard modules
from os.path import join, expanduser

# 3rd party modules

# original modules


config = {
    'max_upload_byte' : 4 * 1e6,  # must be multiply of 4

    # temporary image (before cap is chopped)
    'tmpimg_dir'         : join(expanduser('~'), 'CapMoeTmpImg'),
    'max_tmpimg_size'    : (800, 800),
    'tmpimg_pillow_type' : 'JPEG',

    # cap image candidates
    'max_capimg_candidates' : 5,

    # cap image
    'capimg_dir'    : join(expanduser('~'), 'CapMoeImg'),
    'capimg_suffix' : join(expanduser('~'), 'CapMoeImg'),
}
