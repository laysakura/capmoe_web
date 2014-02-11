# -*- coding: utf-8 -*-
"""
    :synopsis: Unit tests for models of CapMoe

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


# constants
UP_IMAGE_DIR = join(dirname(__file__), 'images')
TMPIMG_DIR   = join(gettempdir(), 'test_upload_tmpimg')


def setup():
    if not os.path.exists(TMPIMG_DIR):
        os.mkdir(TMPIMG_DIR)
    config['tmpimg_dir']      = TMPIMG_DIR
    config['max_upload_byte'] = 500 * 1e3


def teardown():
    shutil.rmtree(TMPIMG_DIR)


def test_upload_tmpimg_get():
    """GET to /upload/
    """
    c   = Client()
    res = c.get('/upload/')
    ns.eq_(res.status_code, 200)


@parameterized([
    '1a.jpg',
    '1b.jpg',  # small size: not resized
])
def test_upload_tmpimg_post(up_img_name):
    """POST to /upload/
    """
    c   = Client()

    # POST image file
    with open(join(UP_IMAGE_DIR, up_img_name), 'rb') as f:
        res = c.post('/upload/', {'img_file': f})

    # should redirect to /upload/<tmpimg_id>
    ns.eq_(res.status_code, 302)
    tmpimg_id = basename(res['Location'])
    ns.ok_(res['Location'].endswith('/upload/%s' % (tmpimg_id)))

    # check temporary image
    path = join(TMPIMG_DIR, tmpimg_id)
    img  = Image.open(path)
    ns.eq_(img.format, 'JPEG')
    ns.ok_(img.size[0] <= config['max_tmpimg_size'][0] and
           img.size[1] <= config['max_tmpimg_size'][1])


def test_upload_tmpimg_post_no_file():
    """POST to /upload/ w/o any uploaded file
    """
    c   = Client()

    # POST w/o file
    res = c.post('/upload/', {'img_file': None})

    # should respond w/ 415
    ns.eq_(res.status_code, 415)  # Unsupported Media Type


@parameterized([
    join(UP_IMAGE_DIR, '5c.jpg'),  # too large
    __file__,                      # not an image
])
def test_upload_tmpimg_post_unsupported_file(fpath):
    """POST to /upload/ w/ unsupported file
    """
    c   = Client()

    # POST image file
    with open(fpath, 'rb') as f:
        res = c.post('/upload/', {'img_file': f})

    # should respond w/ 415
    ns.eq_(res.status_code, 415)  # Unsupported Media Type


def test_upload_capimg_get():
    """GET to /upload/<tmpimg_id>
    """
    tmpimg_id = '123abc'

    # prepare a tmporary image
    shutil.copyfile(join(UP_IMAGE_DIR, '1b.jpg'), join(TMPIMG_DIR, tmpimg_id))

    c   = Client()
    res = c.get('/upload/%s' % (tmpimg_id))
    ns.eq_(res.status_code, 200)


def test_upload_capimg_get_invalid():
    """GET to /upload/<invalid tmpimg_id>
    """
    tmpimg_id = 'notexistingimage'

    c   = Client()
    res = c.get('/upload/%s' % (tmpimg_id))
    ns.eq_(res.status_code, 404)
