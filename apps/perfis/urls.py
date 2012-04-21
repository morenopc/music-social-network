#!/usr/bin/python
# -*- coding: UTF8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('perfis.views',
    #url(r'^$', 'perfis', name='perfis'),
    url(r'^votar/', 'new_vote', name='new_vote'),
    url(r'^confirma_voto/', 'create_vote', name='create_vote'),
    
)
