#!/usr/bin/python
# -*- coding: UTF8 -*-
from django.utils.translation import ugettext, ugettext_lazy as _
from perfis.models import Musicas
from cadastro.forms import MusicasForm, FotosForm, LinksForm
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.utils.encoding import smart_str, smart_unicode
from pinax.apps.photos.models import Image
from avatar.models import Avatar
from pinax.apps.profiles.models import Profile
from pinax.apps.account.forms import LoginForm
from django.contrib.auth.models import User

#
# Musicas
#
def new_music(request):  
    form=MusicasForm()
    return render_to_response('cadastro/ppassos/new_music.html', RequestContext(request, {'form': form}))

def create_music(request):
    
    error_message=''
    user_name=''
    form=MusicasForm(request.POST)
    
    if not form.is_valid():
        context = RequestContext(request, {'form': form, 'mensagem_erro': error_message})
        return render_to_response('cadastro/ppassos/new_music.html',context)
    
    try:# Precaucao
        user_name=request.user.username
        profile=Profile.objects.get(user=request.user.id)
        
        musicas=form.save(commit=False)
        musicas.perfil_id=profile.id
        musicas.save()
        profile.musicas=musicas
        profile.save()
    except Exception,e:
        error_message=u'<p style="color:#f00 !important;">Desculpe %s, mas houve um erro interno. Por favor entre em contato com sac@webtalentos.com.br.<br>%s</p>' % (user_name,e)
        print error_message
        context = RequestContext(request, {'form': form, 'mensagem_erro': error_message})
        return render_to_response('cadastro/ppassos/new_music.html',context)
    form=FotosForm()
    return render_to_response('cadastro/ppassos/new_photos.html', RequestContext(request, {'form': form}))

@login_required   
def musicas(request):
    if request.method == 'POST':
        return create_music(request)
    else:
        return new_music(request)
#
# Fotos
#
def new_photo(request):  
    form=FotosForm()
    return render_to_response('cadastro/ppassos/new_photos.html', RequestContext(request, {'form': form}))

def create_photo(request):
    
    error_message=''
    user_name=''
    form=FotosForm(request.POST, request.FILES)
    
    if not form.is_valid():
        context = RequestContext(request, {'form': form, 'mensagem_erro': error_message})
        return render_to_response('cadastro/ppassos/new_photos.html',context)
    
    try:
        user_name=request.user.username
        member=User.objects.get(pk=request.user.id)
        
        if 'foto_perfil' in request.FILES:
            photo_profile=Avatar()
            photo_profile.avatar=request.FILES['foto_perfil']
            photo_profile.user=member
            photo_profile.primary=True
            photo_profile.save()
        
        if 'foto_divulgacao01' in request.FILES:
            photo=Image()
            photo.title=u'Foto de divulgação 01'
            photo.image=request.FILES['foto_divulgacao01']
            photo.member=member
            photo.save()
        
        if 'foto_divulgacao02' in request.FILES:
            photo=Image()
            photo.title=u'Foto de divulgação 02'
            photo.image=request.FILES['foto_divulgacao02']
            photo.member=member
            photo.save()
    except Exception,e:
        error_message=u'<p style="color:#f00 !important;">Desculpe %s, mas houve um erro interno. Por favor entre em contato com sac@webtalentos.com.br.<br>%s</p>' % (user_name,e)
        context = RequestContext(request, {'form': form, 'mensagem_erro': error_message})
        return render_to_response('cadastro/ppassos/new_photos.html',context)
    
    form=LinksForm()
    return render_to_response('cadastro/ppassos/new_links.html', RequestContext(request, {'form': form }))

@login_required
def fotos(request):
    if request.method == 'POST':
        if request.POST.get("action") == "upload":
            return create_photo(request)
    else:
        return new_photo(request)
        
#
# Links
#
def new_link(request):  
    form=LinksForm()
    return render_to_response('cadastro/ppassos/new_links.html', RequestContext(request, {'form': form}))

def create_link(request):
    
    error_message=''
    user_name=''
    form=LinksForm(request.POST)
    
    if not form.is_valid():
        context = RequestContext(request, {'form': form, 'mensagem_erro': error_message})
        return render_to_response('cadastro/ppassos/new_links.html',context)
    
    try:
        user_name=request.user.username
        profile=Profile.objects.get(user=request.user.id)
        
        perfil=Profile.objects.get(pk=profile.id)
        perfil.website=form.cleaned_data['site']
        perfil.orkut=form.cleaned_data['orkut']
        perfil.twitter=form.cleaned_data['twitter']
        perfil.facebook=form.cleaned_data['facebook']
        perfil.save()
    except Exception,e:
        error_message=u'<p style="color:#f00 !important;">Desculpe %s, mas houve um erro interno. Por favor entre em contato com sac@webtalentos.com.br.<br>%s</p>' % (user_name,e)
        context = RequestContext(request, {'form': form, 'mensagem_erro': error_message})
        return render_to_response('cadastro/ppassos/new_photos.html',context)
    
    return redirect('/about/what_next/')

@login_required
def links(request):
    if request.method == 'POST':
        return create_link(request)
    else:
        return new_link(request)
