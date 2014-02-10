# -*- coding: utf-8 -*-
"""
    capmoe_app.views
    ~~~~~~~~~~~~~~~~

    :synopsis: Describes what data to show

    See: https://docs.djangoproject.com/en/dev/faq/general/#django-appears-to-be-a-mvc-framework-but-you-call-the-controller-the-view-and-the-view-the-template-how-come-you-don-t-use-the-standard-names
"""


# python 2.x support
from __future__ import division, print_function, absolute_import, unicode_literals

# standard modules
import logging

# 3rd party modules
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

# original modules
from capmoe_app.upload.forms import UploadTmpImgForm, UploadCapImgForm
import capmoe_app.errors as err
from capmoe_app.upload.handlers import (
    save_uploaded_tmpimg,
    gen_capimg_candidates
)


# global variables
logger = logging.getLogger('raibow')


def upload_tmpimg(request):
    """Page to upload temporary (not cap-chopped) image
    """
    if request.method == 'POST':
        return upload_tmpimg_post(request)

    form = UploadTmpImgForm()
    return render_to_response(
        'upload_tmpimg.html',
        context_instance=RequestContext(request, {'form': form}))


def upload_tmpimg_post(request):
    """Save POSTed image temporarily
    """
    form = UploadTmpImgForm(request.POST, request.FILES)
    if not form.is_valid():
        logger.debug('Unsupported image is uploaded')
        return HttpResponse(
            'You uploaded non-supported image file',
            status=415)

    try:
        tmpimg_id = save_uploaded_tmpimg(request.FILES['img_file'])
    except err.TooLargeUploadError as e:
        logger.debug(e)
        return HttpResponse(str(e), status=415)
    except Exception as e:  # pragma: no cover
        logger.error('Unexpected error: %s' % (e))
        raise  # 500 error

    return HttpResponseRedirect('/upload/%s' % (tmpimg_id))


def upload_capimg(request, tmpimg_id):
    """Page to choose/chop cap image & upload it
    """
    if request.method == 'POST':
        return upload_capimg_post(request)

    try:
        capimg_candidate_ids = gen_capimg_candidates(tmpimg_id)
    except err.TmpImgNotFoundError as e:
        logger.debug('Requested non-exisiting tmpimg (%s)' % (tmpimg_id))
        raise Http404
    except Exception as e:  # pragma: no cover
        logger.error('Unexpected error: %s' % (e))
        raise  # 500 error

    form = UploadCapImgForm()
    return render_to_response(
        'upload_capimg.html',
        context_instance=RequestContext(request, {
            'form'                 : form,
            'tmpimg_id'            : tmpimg_id,
            'capimg_candidate_ids' : capimg_candidate_ids}))


def upload_capimg_post(request):
    """Extract only cap from temporary image, and save it
    """
    # formにhidden属性でcapの(X,Y,R)があって、それを見て切り出した画像をdbにぶっこむ
    pass
