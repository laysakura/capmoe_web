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
import logging

# 3rd party modules
from PIL import Image, ImageDraw

# original modules
from capmoe_app.config import config
import capmoe_app.utils as utils
import capmoe_app.errors as err
from capmoe_app.models import CapImage


# global variables
logger = logging.getLogger('raibow')


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
    path = join(config['tmpimg_dir'], tmpimg_id)
    img.save(path, config['tmpimg_pillow_type'])

    return tmpimg_id


def gen_capimg_candidates(tmpimg_id):
    """Generate candidate cap images

    :returns: [{'id': 'capimg_candidate_id',
               'x': candidate_x, 'y': candidate_y, 'r': candidate_r},
               ...
              ]
    :raises: :class:`TmpImgNotFoundError` when temporary image file
        corresponding to :param:`tmpimg_id` is not found
    """
    def gen_capimg_candidate(tmpimg_path, circle):
        """Generate img and return its id
        """
        x, y, r = (circle['x'], circle['y'], circle['r'])

        # crop box containing cap circle
        img = Image.open(tmpimg_path).crop((x - r, y - r, x + r, y + r))
        img = img.resize(config['capimg_candidate_size'])

        capimg_candidate_path = '%s%s' % (tmpimg_path, utils.randstr(length=5))
        img.save(capimg_candidate_path, config['tmpimg_pillow_type'])
        return basename(capimg_candidate_path)

    tmpimg_path = join(config['tmpimg_dir'], tmpimg_id)
    if not exists(tmpimg_path):
        raise err.TmpImgNotFoundError('No such file: %s' % (tmpimg_path))

    import capmoe.api  # python interpreter who import `capmoe` package
                       # must have access to `cv2` package and so on
    cand_circles = capmoe.api.capdetector(
        tmpimg_path, max_candidates=config['max_capimg_candidates'])
    return [
        {'id': gen_capimg_candidate(tmpimg_path, c),
         'x': c['x'], 'y': c['y'], 'r': c['r']}
        for c in cand_circles]


def register_capimg(tmpimg_id, x, y, r):
    """Crop cap a image from tmporary image and register it to DB

    :returns: capimg_id
    :raises: :class:`InvalidCircleError` when
        circle is not included in temporary image
    """
    tmpimg_path = join(config['tmpimg_dir'], tmpimg_id)
    if not exists(tmpimg_path):
        raise err.TmpImgNotFoundError('No such file: %s' % (tmpimg_path))

    # crop box containing cap circle
    img = Image.open(tmpimg_path)
    if (r <= 0 or
        x - r < 0 or x + r >= img.size[0] or
        y - r < 0 or y + r >= img.size[1]
    ):
        raise err.InvalidCircleError(
            'Circle (%d, %d, %d) is invalid for image size (%d, %d)' %
            (x, y, r, img.size[0], img.size[1]))
    img = img.crop((x - r, y - r, x + r, y + r)).resize(config['capimg_size'])

    # mask non-cap area
    foreground = Image.new('RGB', img.size, (0, 0, 255))
    mask       = Image.new('L', img.size, 0)
    draw       = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + img.size, fill=255)
    masked_img = Image.composite(img, foreground, mask)

    # insert record for the masked image, and get id of it
    record = CapImage()
    record.save()
    capimg_id = record.id

    # save masked cap image
    capimg_path = join(config['capimg_dir'], '%d.%s' %
                       (capimg_id, config['capimg_suffix']))
    assert(not exists(capimg_path))
    masked_img.save(capimg_path, config['capimg_pillow_type'])

    return capimg_id
