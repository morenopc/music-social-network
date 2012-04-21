from django.contrib import admin
from perfis.models import ListaCategoria, ListaEstilos, ListaAutoria, Musicas

class MusicasAdmin(admin.ModelAdmin):
    list_display = ('video_id', 'estilo', 'mnome','perfil')
    search_fields = ('video_id','mnome')

admin.site.register(Musicas,MusicasAdmin)
admin.site.register(ListaCategoria)
admin.site.register(ListaEstilos)
admin.site.register(ListaAutoria)
