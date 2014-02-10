# -*- coding: utf-8 -*-
"""
    capmoe_app.upload.forms
    ~~~~~~~~~~~~~~~~~~~~~~~

    :synopsis: Forms

    Description.
"""


# python 2.x support
from __future__ import division, print_function, absolute_import, unicode_literals

# standard modules

# 3rd party modules
from django import forms

# original modules


class UploadTmpImgForm(forms.Form):
    """Form to upload temporary image containing cap
    """
    img_file = forms.ImageField()


class UploadCapImgForm(forms.Form):
    """Form to chop a cap from temporary image, and upload it
    """
    cap_x = forms.IntegerField(widget=forms.HiddenInput())
    cap_y = forms.IntegerField(widget=forms.HiddenInput())
    cap_r = forms.IntegerField(widget=forms.HiddenInput())
