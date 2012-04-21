# -*- coding: UTF8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('videos.views',
    url(r'^$', 'videos', name='videos'),
    url(r'(\d+)/$', 'videos', name='videos'),
    url(r'(\d+)/(.{11})/$', 'videos', name='videos'),
    #url(r'^confirma_voto/', 'create_vote', name='create_vote'),
    
)
