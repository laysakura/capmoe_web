# -*- coding: utf-8 -*-
"""
    capmoe_app.models
    ~~~~~~~~~~~~~~~~~

    :synopsis: Models for CapMoe web service

    Description.
"""


# standard modules
import os

# 3rd party modules
from django.db import models

# original modules
from capmoe_app.config import config


class CapImage(models.Model):
    """Cap's images"""
    # [todo] - feature vector column?

    def img_path(self):
        return os.path.join(config['img_dir'],
                            '%d.%s' % (self.id, config['img_suffix']))

    def thumb_path(self):
        return os.path.join(config['thumb_dir'],
                            '%d.%s' % (self.id, config['img_suffix']))
