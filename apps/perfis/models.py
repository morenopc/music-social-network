#!/usr/bin/python
# -*- coding: UTF8 -*-
from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _
from profiles.models import Profile

CATEGORIAS=(
    ('Cantor','Cantor'),
    ('Cantora','Cantora'),
    ('Dupla','Dupla'),
    ('Banda','Banda'),
    ('Grupo','Grupo'),
    ('Instrumentista','Instrumentista'),
    ('Outro','Outro'),
)
class ListaCategoria(models.Model):
    lcategoria=models.CharField(max_length=32, choices=CATEGORIAS)
    def __unicode__(self):
        return self.lcategoria

ESTILOS=(
    (u'Rock','Rock'),
    (u'Pop','Pop'),
    (u'Heavy Metal','Heavy Metal'),
    (u'Punk Rock','Punk Rock'),
    (u'Blues','Blues'),
    (u'Instrumental','Instrumental'),
    (u'Romântica','Romantica'),
    (u'Eletrônico','Eletronico'),
    (u'Sertanejo','Sertanejo'),
    (u'Pagode','Pagode'),
    (u'MPB','MPB'),
    (u'Jazz','Jazz'),
    (u'Reggae','Reggae'),
    (u'Erudita','Erudita'),
    (u'Samba','Samba'),
    (u'R&B','R&B'),
    (u'Axé','Axe'),
    (u'Country','Country'),
    (u'Bossa Nova','Bossa Nova'),
    (u'New Age','New Age'),
)
class ListaEstilos(models.Model):
    lestilos=models.CharField(max_length=32, choices=ESTILOS)
    def __unicode__(self):
        return self.lestilos

MAUTORIA=(
    (u'Própria/Inédita',u'Própria/Inédita'),
    (u'Cover de outro artista',u'Cover de outro artista'),
)
class ListaAutoria(models.Model):
    lautoria=models.CharField(max_length=32, choices=MAUTORIA)
    def __unicode__(self):
        return self.lautoria

class Musicas(models.Model):

    perfil=models.ForeignKey(Profile, verbose_name=_(u'Perfil'))
    release=models.TextField(_(u'Release'), blank=True)
    estilo=models.ForeignKey(ListaEstilos, verbose_name=_(u'Estilo musical'))
    categoria=models.ForeignKey(ListaCategoria, verbose_name=_(u'Categoria musical'), blank=True, null=True)
    mnome=models.CharField(_(u'Nome da música'), max_length=56, blank=True)
    mautor=models.CharField(_(u'Autor(es) da música'), max_length=128, blank=True)
    mautoria=models.ForeignKey(ListaAutoria, verbose_name=_(u'Sua música é'), blank=True, null=True)
    video=models.URLField(_(u'Vídeo'), help_text=_(u'Adicione seu vídeo colando o link do YouTube'))
    video_id=models.CharField(_(u'ID do vídeo'), max_length=11, unique=True)
    votos=models.PositiveIntegerField(_(u'Votos'), default=0)
    data_criacao=models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name = u"Música"
    
    def __unicode__(self):
        return '%s %s' % (self.mnome, self.estilo)
    
