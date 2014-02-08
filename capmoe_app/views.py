# -*- coding: utf-8 -*-
"""
    capmoe_app.views
    ~~~~~~~~~~~~~~~~

    :synopsis: Describes what data to show

    See: https://docs.djangoproject.com/en/dev/faq/general/#django-appears-to-be-a-mvc-framework-but-you-call-the-controller-the-view-and-the-view-the-template-how-come-you-don-t-use-the-standard-names
"""


# standard modules

# 3rd party modules
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

# original modules
from capmoe_app.upload.forms import UploadTmpImgForm
from capmoe_app.upload.handlers import save_uploaded_tmpimg


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
        return HttpResponse(status=415)  # Unsupported Media Type

    try:
        tmpimg_id = save_uploaded_tmpimg(request.FILES['img_file'])
    except AttributeError:
        return HttpResponse(status=415)  # too large; Unsupported Media Type

    return HttpResponseRedirect('/upload/%s' % (tmpimg_id))


def upload_capimg(request, tmpimg_id):
    """Page to choose/chop cap image & upload it
    """
    if request.method == 'POST':
        return upload_capimg_post(request)

    pass

def upload_capimg_post(request):
    """Extract only cap from temporary image, and save it
    """
    pass
