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


urlpatterns = patterns(
    '',

    url(r'^upload/done/(?P<capimg_id>[\d\w]+)' , upload_views.upload_done),
    url(r'^upload/(?P<tmpimg_id>[\d\w]+)'      , upload_views.upload_capimg),
    url(r'^upload/'                            , upload_views.upload_tmpimg),
)
