#!/usr/bin/python
# -*- coding: UTF8 -*-
from django.utils.translation import ugettext, ugettext_lazy as _
from player.models import Configuracoes
from perfis.models import Musicas, ESTILOS
from homepage.forms import VoteForm
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.core.validators import EMPTY_VALUES
from django.views.decorators.csrf import csrf_protect, csrf_exempt

#
# Vote
#
@csrf_protect
def new_vote(request):
    """
    Request new vote
    """

    if not request.method == 'POST':
        return render_to_response('homepage/vote_error.html')
    
    video=request.POST.get('video_id')
    form=VoteForm()
    try:
        musica=Musicas.objects.get(video_id=video)
    except:
        musica=Musicas()# Default
    
    return render_to_response('homepage/vote.html', RequestContext(request, {'musica': musica,'form':form}))

@csrf_protect
def create_vote(request):
    """
    Request new vote
    """
    if not request.method == 'POST':
        return render_to_response('homepage/vote_error.html')
    
    form = VoteForm(request.POST)
    if form.is_valid():
    
        video=form.cleaned_data.get('video_id')
        try:
            musica=Musicas.objects.get(video_id=video)
            musica.votos=musica.votos+1
            musica.save()
        except:
            return render_to_response('homepage/vote_error.html')

        return render_to_response('homepage/vote_success.html', RequestContext(request))

    form=VoteForm()
    m='Tente novamente'
    try:
        musica=Musicas.objects.get(video_id=request.POST.get('video_id'))
    except:
        return render_to_response('homepage/vote_error.html')
    return render_to_response('homepage/vote.html', RequestContext(request, {'musica': musica,'form':form,'m':m}))

#def vote(request):
#    if request.method == 'POST':
#        return create_vote(request)
#    else:
#        return new_vote(request)
