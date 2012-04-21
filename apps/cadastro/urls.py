#!/usr/bin/python
# -*- coding: UTF8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('cadastro.views',
    url(r'^musicas/', 'musicas', name='Musicas'),
    url(r'^fotos/', 'fotos', name='Fotos'),
    url(r'^links/', 'links', name='Links'),
)
