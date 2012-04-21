#!/usr/bin/python
# -*- coding: UTF8 -*-
from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _
from colors.fields import ColorField

class Configuracoes(models.Model):

    playerapiid=models.CharField(_(u'Nome do Player'), max_length=12, blank=True, default='Default')
    width=models.SmallIntegerField(_(u'Largura'), default=480)
    height=models.SmallIntegerField(_(u'Altura'), default=390)
    video_id=models.CharField(_(u'ID do vídeo'), max_length=11, default='EgJxKW8RuUM')
    autohide=models.SmallIntegerField(_(u'Controles'), choices=((0, u'Sempre visível'), (1, 'Visível no início'), (2, 'Visível')), default=2)
    autoplay=models.SmallIntegerField(_(u'Auto Play'), choices=((0, u'Desligado'), (1, 'Ligado')), default=0)
    border=models.SmallIntegerField(_(u'Borda'), choices=((0, u'Desligado'), (1, 'Ligado')), default=0)
    cc_load_policy=models.CharField(_(u'Forçar legendas'), max_length=24,choices=(('&cc_load_policy=1', u'Sempre visível'), ('', 'Opcional')), blank=True, default='')
    color1=ColorField(_(u'Cor Borda 1'), default='ffffff')
    color2=ColorField(_(u'Cor Borda 2'), default='ffffff')
    controls=models.SmallIntegerField(_(u'Controles'), choices=((0, u'Desligado'), (1, 'Ligado')), default=1)
    disablekb=models.SmallIntegerField(_(u'Atalhos de teclado'), choices=((0, u'Desligado'), (1, 'Ligado')), default=0)
    enablejsapi=models.SmallIntegerField(_(u'Ativar JavaScript API'), choices=((0, u'Desligado'), (1, 'Ligado')), default=0)
    egm=models.SmallIntegerField(_(u'Menu Genie'), choices=((0, u'Desligado'), (1, 'Ligado')), default=0)
    fs=models.SmallIntegerField(_(u'Permitir tela cheia'), choices=((0, u'Desligado'), (1, 'Ligado')), default=0)
    hd=models.SmallIntegerField(_(u'Permitir modo HD'), choices=((0, u'Desligado'), (1, 'Ligado')), default=0)
    iv_load_policy=models.SmallIntegerField(_(u'Anotações no vídeo'), choices=((1, u'Mostrar'), (3, 'Não mostrar')), default=1)
    loop=models.SmallIntegerField(_(u'Repetir'), choices=((0, u'Desligado'), (1, 'Ligado')), default=0)
    modestbranding=models.SmallIntegerField(_(u'Retirar logo do YouTube'), choices=((0, u'Desligado'), (1, 'Ligado')), default=0)
    #origin - rever relacionado com JS API
    playlist= models.CharField(max_length=1200, blank=True, null=True, default='')
    rel=models.SmallIntegerField(_(u'Permitir carregar vídeo relacionados'), choices=((0, u'Desligado'), (1, 'Ligado')), default=1)
    showinfo=models.SmallIntegerField(_(u'Mostrar informações'), choices=((0, u'Desligado'), (1, 'Ligado')), default=0)
    showsearch=models.SmallIntegerField(_(u'Mostrar pesquisa'), choices=((0, u'Desligado'), (1, 'Ligado')), default=1)
    start=models.IntegerField(_(u'Iniciar em'), null=True, blank=True, help_text='Segundos')
    version=models.SmallIntegerField(_(u'Versão'), default=3)
    
    class Meta:
        #ordering = ["created_at"]
        verbose_name = u"Configuração"
        verbose_name_plural = u"Configurações"
    
    def __unicode__(self):
        return self.playerapiid
    
