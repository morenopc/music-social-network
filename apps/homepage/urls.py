#!/usr/bin/python
# -*- coding: UTF8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('homepage.views',
    url(r'^$', 'homepage', name='home'),
    url(r'^xhr_musicas/', 'xhr_musicas', name='xhr_musicas'),
    url(r'^(.{11})/videoinfo/$', 'video_info', name='video_info'),
    url(r'^(.{11})/comentario/$', 'comment', name='comment'),
)
