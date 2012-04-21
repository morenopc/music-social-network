#!/usr/bin/python
# -*- coding: UTF8 -*-
from django.utils.translation import ugettext, ugettext_lazy as _
from player.models import Configuracoes
from perfis.models import Musicas, ESTILOS
from homepage.forms import VoteForm
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.core.validators import EMPTY_VALUES
from django.core import serializers
from django.db.models import Sum
from django.views.decorators.csrf import csrf_protect, csrf_exempt

#
# Homepage
#
@csrf_protect
def homepage(request):
    """
    Top 30
    """
    titulo='Top 30'
    vform=VoteForm()
    ms=['']
    other_user='moreno'
    
    est=request.GET.get('op')
    rkms=Musicas.objects.all().order_by('-votos')[:30]# Default Top30
    tvotes=rkms.aggregate(Sum('votos'))["votos__sum"]
    
    if est in EMPTY_VALUES:
        ms=rkms
    else:
        titulo=ESTILOS[int(est)-1][0]
        ms=Musicas.objects.filter(estilo=est).order_by('-votos')[:30]
        #if len(ms) > 0:
        #    titulo=ms[0].estilo
    jspl=''
    pl=''
    ims=[]
    # Pensando Json
    #json=serializers.serialize("json", Musicas.objects.filter(pk=1))
    
    try:
        player=Configuracoes.objects.get(pk=1)
    except:
        player=Configuracoes()# Default
    
    if len(ms) == 1:
        ims=iter(ms)
        player.video_id=ims.next().video_id
        jspl="'"+player.video_id+"'" # o jspl[0] deve ser o primeiro video 'player.video_id'
        
    elif len(ms) > 1:
        ims=iter(ms)
        player.video_id=ims.next().video_id
        jspl="'"+player.video_id+"'"
        pl=str(ims.next().video_id)
        jspl+=",'"+pl+"'"
        
        for m in ims:
            pl+=','+m.video_id
            jspl+=",'"+m.video_id+"'"
    else:
    # Estilo nao possui musicas no momento
    # Estudar tratamento de excecao no pinax
    # raise?
        player.video_id='PQLMFNC2Awo'
        jspl="'"+player.video_id+"'"
    
    player.playlist=pl
    player.save()
    
    #if len(ms) > 1:
    #    pl=str(ims.next().video_id)
    #    jspl="'"+pl+"'"
    #
    #for m in ims:
    #    pl+=','+m.video_id
    #    jspl+=",'"+m.video_id+"'"
    #
    
    return render_to_response('homepage.html', RequestContext(request, {
        'titulo':titulo,
        'player': player,
        'musicas':rkms,
        'total_votos':tvotes,
        'menu':ESTILOS,
        'jsPlaylist':jspl,
        'form':vform,
        'video':ms[0],
        'other_user':other_user
        }))
    
def xhr_musicas(request):
    
    if request.is_ajax():
        message = "Hello AJAX"
    else:
        message = "Hello"
    return HttpResponse(message)

def video_info(request, video_id):
    video=get_object_or_404(Musicas, video_id=video_id)
    return render_to_response('comments/info_ajax_table.html', RequestContext(request, {'video':video}))
    
def comment(request, video_id):
    video=get_object_or_404(Musicas, video_id=video_id)
    return render_to_response('comments/comment_ajax_form.html', RequestContext(request, {'video':video}))
