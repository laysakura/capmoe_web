# -*- coding: utf-8 -*-
"""
    :synopsis: Unit tests for models ofCapMoe

    Description.
"""


# standard modules
from os.path import join

# 3rd party modules
import nose.tools as ns

# original modules
from capmoe_app.config import config
from capmoe_app.models import CapImage


def setUp(self):
    CapImage.objects.create()
    CapImage.objects.create()


def test_file_path():
    record = CapImage.objects.get(id=1)
    ns.eq_(record.img_path(),
           join(config['img_dir'], '1.' + config['img_suffix']))
