# -*- coding: utf-8 -*-
"""
    :synopsis: Unit tests for models of CapMoe

    Description.
"""


# python 2.x support
from __future__ import division, print_function, absolute_import, unicode_literals

# standard modules
from os.path import join

# 3rd party modules
import nose.tools as ns

# original modules
from capmoe_app.config import config, STATIC_DIR
from capmoe_app.models import CapImage


def setUp(self):
    CapImage.objects.create()
    CapImage.objects.create()


def test_file_path():
    record = CapImage.objects.get(id=1)
    ns.eq_(record.capimg_path(),
           join(STATIC_DIR, config['capimg_dirname'],
                '1.%s' % (config['capimg_suffix'])))
