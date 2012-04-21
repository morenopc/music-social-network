# -*- coding: UTF8 -*-
from django.utils.translation import ugettext, ugettext_lazy as _
from player.models import Configuracoes
from perfis.models import Musicas, ESTILOS
from homepage.forms import VoteForm
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.core.validators import EMPTY_VALUES
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

#
# Videos
#
@login_required
def videos(request,*args):
    """
    videos
    """
    
    titulo=u'Seus vídeos'
    #vform=VoteForm()
    ms=['']
    first_video=None
    #other_user='moreno'
    video_request=[]
    
    try:
        player=Configuracoes.objects.get(pk=1)
    except:
        player=Configuracoes()# Default
    
    ms=Musicas.objects.filter(perfil__user=request.user.id).order_by('-votos')
    if len(ms)>0:
        first_video=ms[0]
    
    if len(args) == 1:
        try:
            ms=Musicas.objects.filter(perfil__user=args[0]).order_by('-votos')
            if args[0] != request.user.id:
                #try:
                u=User.objects.get(pk=args[0])
                titulo=str(u.username)+u' vídeos'
                #except:
                #    pass
        except:
            pass
    elif len(args) == 2:
        try:
            video_request=Musicas.objects.get(perfil__user=args[0],video_id=args[1])
            ms=Musicas.objects.filter(perfil__user=request.user.id).exclude(video_id=args[1]).order_by('-votos')
        except:
            pass
    
    jspl=''
    pl=''
    ims=[]
    
    if len(ms) == 1:
        #ims=iter(ms)
        player.video_id=ms[0].video_id
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
        player.video_id=''
        jspl="''"
    
    if video_request:
        pl=player.video_id+','+pl
        player.video_id=video_request.video_id
        jspl="'"+video_request.video_id+"',"+jspl
    
    player.playlist=pl
    player.save()
    
    local_tags={
     'titulo':titulo,
     'player':player,
     'musicas':ms,
     #'total_votos':tvotes,
     #'menu':ESTILOS,
     'jsPlaylist':jspl,
     #'form':vform,
     'video':first_video, # se vazio ERROR list index out of range
     #'other_user':other_user
     }
    
    return render_to_response('videos/videos.html', RequestContext(request,local_tags))
    
