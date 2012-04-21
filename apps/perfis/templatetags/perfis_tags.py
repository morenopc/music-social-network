from django import template
from perfis.models import Musicas
register=template.Library()

@register.filter
def public_musics(parser):
    return Musicas.objects.filter(perfil__user=parser).order_by('-votos')

@register.filter
def len_musics(parser):
    return len(Musicas.objects.filter(perfil__user=parser))
