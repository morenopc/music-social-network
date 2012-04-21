#!/usr/bin/python
# -*- coding: UTF8 -*-
from django import forms
from django.utils.translation import ugettext, ugettext_lazy as _
from perfis.models import Musicas

class MusicasForm(forms.ModelForm):
    video_id=forms.CharField(label=u'ID do vídeo', widget=forms.TextInput(attrs={'readonly':'readonly'}), required=False)#widget=forms.HiddenInput()
    class Meta:
        model=Musicas
        exclude=('perfil','votos')

class FotosForm(forms.Form):
    foto_perfil=forms.ImageField(label=_(u'Foto do perfil'), help_text=_(u'Para redimencionar use http://mypictr.com/'))
    foto_divulgacao01=forms.ImageField(label=_(u'Foto de divulgação'),required=False, help_text=_(u'Para redimencionar use http://mypictr.com/'))
    foto_divulgacao02=forms.ImageField(label=_(u'Outra foto de divulgação'),required=False, help_text=_(u'Para redimencionar use http://mypictr.com/'))

class LinksForm(forms.Form):
    site=forms.URLField(label=_(u'Site pessoal'), required=False)
    orkut=forms.URLField(label=_(u'Orkut'), required=False)
    twitter=forms.URLField(label=_(u'Twitter'), required=False)
    facebook=forms.URLField(label=_(u'Facebook'), required=False)
