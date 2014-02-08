# -*- coding: utf-8 -*-
"""
    capmoe_app.upload.forms
    ~~~~~~~~~~~~~~~~~~~~~~~

    :synopsis: Forms

    Description.
"""


# standard modules

# 3rd party modules
from django import forms

# original modules


class UploadTmpImgForm(forms.Form):
    """Upload any image
    """
    img_file = forms.ImageField()
