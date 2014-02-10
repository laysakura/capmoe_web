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
    circle_choice = forms.ChoiceField(
        choices=[
            ('candidate1', 'candidate 1'),
            ('candidate2', 'candidate 2'),
            ('candidate3', 'candidate 3'),
            ('candidate4', 'candidate 4'),
            ('candidate5', 'candidate 5'),
        ],
        widget=forms.RadioSelect())
