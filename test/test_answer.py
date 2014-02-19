# -*- coding: utf-8 -*-
"""
    :synopsis: Unit tests for /answer view

    Description.
"""


# python 2.x support
from __future__ import division, print_function, absolute_import, unicode_literals

# standard modules
import os
from os.path import basename, dirname, join
from tempfile import gettempdir
import shutil

# 3rd party modules
import nose.tools as ns
from nose_parameterized import parameterized
from django.test.client import Client
from PIL import Image

# original modules
from capmoe_app.config import config
from capmoe_app import utils


# constants
UP_IMAGE_DIR = join(dirname(__file__), 'images')
TMPIMG_DIR   = join(gettempdir(), 'test_upload_tmpimg')
CAPIMG_DIR   = join(gettempdir(), 'test_upload_capimg')


def setup():
    if not os.path.exists(TMPIMG_DIR):
        os.mkdir(TMPIMG_DIR)
    if not os.path.exists(CAPIMG_DIR):
        os.mkdir(CAPIMG_DIR)
    config['tmpimg_dir']      = TMPIMG_DIR
    config['capimg_dir']      = CAPIMG_DIR
    config['max_upload_byte'] = 500 * 1e3


def teardown():
    shutil.rmtree(TMPIMG_DIR)
    shutil.rmtree(CAPIMG_DIR)


def test_upload_done_get():
    """GET to /answer/<capimg_id>
    """
    capimg_id = '1234abcd'

    # prepare cap image
    shutil.copyfile(
        join(UP_IMAGE_DIR, '1a.jpg'),
        join(CAPIMG_DIR, '%s.%s' % (capimg_id, config['capimg_suffix'])))

    c   = Client()
    res = c.get('/answer/%s' % (capimg_id))
    ns.eq_(res.status_code, 200)


@parameterized([
    'notexistingimage',
    ''
])
def test_upload_done_get_invalid(capimg_id):
    """GET to /answer/<invalid_capimg_id>
    """
    c   = Client()
    res = c.get('/answer/%s' % (capimg_id))
    ns.eq_(res.status_code, 404)
