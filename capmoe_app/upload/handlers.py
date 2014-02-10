# -*- coding: utf-8 -*-
"""
    capmoe_app.upload.handlers
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    :synopsis: Handler working when cap image is uploaded

    Description.
"""


# python 2.x support
from __future__ import division, print_function, absolute_import, unicode_literals

# standard modules
from os.path import join, exists, basename
import io

# 3rd party modules
from PIL import Image, ImageDraw

# original modules
from capmoe_app.config import config
import capmoe_app.utils as utils
import capmoe_app.errors as err


def save_uploaded_tmpimg(f):
    """Temporarily save uploaded image.

    Temporary images are really saved after cap circle is chopped.

    :returns: temporary image id string
    :raises: :class:`TooLargeUploadError` when uploaded file is too large
    """
    if f.size > config['max_upload_byte']:
        raise err.TooLargeUploadError(
            'Uploaded file is too large (%d bytes). Up to %d bytes' %
            (f.size, config['max_upload_byte']))

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


def gen_capimg_candidates(tmpimg_id):
    """Generate candidate cap images

    :returns: ['capimg_candidate_id', ...]
    :raises: :class:`TmpImgNotFoundError` when temporary image file
        corresponding to :param:`tmpimg_id` is not found
    """
    def gen_capimg_candidate(tmpimg_path, circle):
        """Generate img and return its id
        """
        x, y, r = (circle['x'], circle['y'], circle['r'])

        img = Image.open(tmpimg_path).crop((x - r, y - r, x + r, y + r))
        img = img.resize(config['capimg_candidate_size'])

        capimg_candidate_path = '%s%s' % (tmpimg_path, utils.randstr(length=5))
        img.save(capimg_candidate_path, config['tmpimg_pillow_type'])
        return basename(capimg_candidate_path)

    tmpimg_path = join(config['tmpimg_dir'], str(tmpimg_id))
    if not exists(tmpimg_path):
        raise err.TmpImgNotFoundError('No such file: %s' % (tmpimg_path))

    import capmoe.api
    cand_circles = capmoe.api.capdetector(
        tmpimg_path, max_candidates=config['max_capimg_candidates'])
    return [gen_capimg_candidate(tmpimg_path, c) for c in cand_circles]
