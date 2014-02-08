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
from django.shortcuts import render

# original modules


def upload(request):
    return HttpResponse("It works!!")
