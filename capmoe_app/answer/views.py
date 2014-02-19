# -*- coding: utf-8 -*-
"""
    capmoe_app.views
    ~~~~~~~~~~~~~~~~

    :synopsis: View to check similar caps
"""


# python 2.x support
from __future__ import division, print_function, absolute_import, unicode_literals

# standard modules
import logging

# 3rd party modules
from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext

# original modules
import capmoe_app.errors as err
import capmoe_app.utils as utils


# global variables
logger = logging.getLogger('raibow')


def answer(request, capimg_id):
    """Page to check similar caps
    """
    try:
        capimg_name = utils.get_capimg_name(capimg_id)
    except err.CapImgNotFoundError as e:
        logger.debug('Requested non-exisiting capimg (%s)' % (e))
        raise Http404
    except Exception as e:  # pragma: no cover
        logger.error('Unexpected error: %s' % (e))
        raise  # 500 error

    return render_to_response(
        'answer.html',
        context_instance=RequestContext(request, {
            'capimg_name': capimg_name}))
