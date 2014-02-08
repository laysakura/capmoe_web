# -*- coding: utf-8 -*-
"""
    capmoe_app.upload.handlers
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    :synopsis: Handler working when cap image is uploaded

    Description.
"""


# standard modules
from os.path import join
import io

# 3rd party modules
from PIL import Image

# original modules
from capmoe_app.config import config
import capmoe_app.utils as utils


def save_uploaded_tmpimg(f):
    """Temporarily save uploaded image.

    Temporary images are really saved after cap circle is chopped.

    :returns: temporary image id string
    :raises: `AttributeError` when invalid image is uploaded
    """
    if f.size > config['max_upload_byte']:
        raise AttributeError('Uploaded file is too large (%d bytes)' %
                             (f.size))

    # resize
    img_stream = io.BytesIO(f.read())
    img        = Image.open(img_stream)
    newsize    = utils.shrinked_size(img.size, config['max_tmpimg_size'])
    if newsize != img.size:
        img = img.resize(newsize)

    # save
    tmpimg_id = utils.randstr(length=10)
    path = join(config['tmpimg_dir'], str(tmpimg_id))
    img.save(path, config['tmpimg_pillow_type'])

    return tmpimg_id
