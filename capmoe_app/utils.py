# -*- coding: utf-8 -*-
"""
    capmoe_app.utils
    ~~~~~~~~~~~~~~~~

    :synopsis: Utility functions/classes

    Description.
"""


# python 2.x support
from __future__ import division, print_function, absolute_import, unicode_literals
from os.path import join, exists, basename

# standard modules
import string
import random

# 3rd party modules

# original modules
from capmoe_app.config import config
import capmoe_app.errors as err


def randstr(length, alphabets=string.digits + string.ascii_letters):
    """Generate random string with length of :param:`length`

    *Example*

    .. code-block: python
        >>> len(randstr(10))
        10
    """
    return ''.join(random.choice(alphabets) for i in range(length))


def shrinked_size(orig_size, max_size):
    """Shrink if too large, keeping x-y ratio

    *Example*

    .. code-block: python
        >>> shrinked_size((800, 400), max_size=(800, 600))
        (800, 400)
        >>> shrinked_size((1600, 400), max_size=(800, 600))
        (800, 200)
        >>> shrinked_size((816, 612), max_size=(800, 800))
        (800, 600)
    """
    scale = max(orig_size[0] / max_size[0], orig_size[1] / max_size[1])
    if scale <= 1.0:
        return orig_size
    return (int(orig_size[0] / scale), int(orig_size[1] / scale))


def get_capimg_name(capimg_id):
    """Get existing cap image name

    :raises: :class:`CapImgNotFoundError` when cap image
        corresponding to :param:`capimg_id` does not exist
    """
    capimg_path = join(config['capimg_dir'],
                       '%s.%s' % (capimg_id, config['capimg_suffix']))
    if not exists(capimg_path):
        raise err.CapImgNotFoundError('No such file: %s' % (capimg_path))
    return basename(capimg_path)
