# -*- coding: utf-8 -*-
"""
    capmoe_app.urls
    ~~~~~~~~~~~~~~~

    :synopsis: URL scheme

    Description.
"""


# python 2.x support
from __future__ import division, print_function, absolute_import, unicode_literals

# standard modules

# 3rd party modules
from django.conf.urls import patterns, url

# original modules
from capmoe_app.upload import views as upload_views
from capmoe_app.answer import views as answer_views


urlpatterns = patterns(
    '',

    url(r'^upload/(?P<tmpimg_id>[\d\w]+)'      , upload_views.upload_capimg),
    url(r'^upload/'                            , upload_views.upload_tmpimg),

    url(r'^answer/(?P<capimg_id>[\d\w]+)', answer_views.answer),
)
