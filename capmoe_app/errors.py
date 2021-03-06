# -*- coding: utf-8 -*-
"""
    capmoe_app.errors
    ~~~~~~~~~~~~~~~~~

    :synopsis: Custom exception classes

    Description.
"""


# python 2.x support
from __future__ import division, print_function, absolute_import, unicode_literals

# standard modules

# 3rd party modules

# original modules


class TooLargeUploadError(AttributeError):
    pass


class TmpImgNotFoundError(IOError):
    pass


class CapImgNotFoundError(IOError):
    pass


class InvalidCircleError(AttributeError):
    pass
