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
from os.path import join, dirname

# 3rd party modules

# original modules


# constants
BASE_DIR = join(dirname(__file__), '..')


config = {
    'max_upload_byte' : 4 * 1e6,  # must be multiply of 4

    # temporary image (before cap is chopped)
    'tmpimg_dir'         : join(BASE_DIR, 'capmoe_app', 'static', 'tmpimg'),
    'max_tmpimg_size'    : (800, 800),
    'tmpimg_pillow_type' : 'JPEG',

    # cap image candidates
    'max_capimg_candidates' : 5,
    'capimg_candidate_size' : (100, 100),

    # cap image
    'capimg_dir'         : join(BASE_DIR, 'capmoe_app', 'static', 'capimg'),
    'capimg_suffix'      : 'jpg',
    'capimg_pillow_type' : 'JPEG',
    'capimg_size'        : (200, 200),
}
