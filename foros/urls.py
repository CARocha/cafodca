from django.conf.urls import url
from django.views.generic import ListView, DetailView
from .models import *
from .views import *

urlpatterns = [
    #url(r'^$', 'index', name='index'),
#     url(r'^$', ListView.as_view(model=Foros, 
#     	                        template_name="foros/foro_list.html"),
#     	                        name='foro-list'),
#     #url(r'^$', 'lista_foro', name='lista-foro'), 
#     url(r'^(?P<pk>\d+)/$', DetailView.as_view(model=Foros, 
#     	                                        template_name='foros/foro_detail.html'),
#                                                 name='foro-detail'),
#     url(r'^crear/$', 'crear_foro', name='crear-foro'),
#     url(r'^editar/(?P<id>\d+)/$', 'editar_foro', name='editar-foro'),
#     url(r'^borrar/(?P<id>\d+)/$', 'borrar_foro', name='borrar-foro'),
#     url(r'^ver/(?P<foro_id>\d+)/$', 'ver_foro', name='ver-foro'),
#     url(r'^ver_comentario/(?P<aporte_id>\d+)/$', 'comentario_foro', name='cometario-foro'),
	url(r'^perfil/$', perfil, name='ver-perfil'),
    url(r'^privado/nota/$', notas_personales, name='notas-personales'),
    url(r'^privado/nota/editar/(?P<id>\d+)/$', notas_personales_editar, name='notas-personales-editar'),
    url(r'^privado/nota/eliminar/(?P<id>\d+)', eliminar_notas_contraparte, name='eliminar-notas-contraparte'),
    url(r'^privado/agenda/$', agenda_personales, name='agenda-personales'),
    url(r'^privado/documento/$', documento, name='documentos'),
#     url(r'^privado/documento_tag/(?P<tags>\w+)/$', 'busqueda_tag', name='busqueda-tag'),
    url(r'^privado/multimedia_fotos/$', multimedia_fotos, name='multimedia_fotos'),
#     url(r'^privado/multimedia_fotos_tag/(?P<tags>\w+)/$', 'multimedia_fotos_tag', name='multimedia_fotos_tag'),
#     url(r'^privado/multimedia_videos/$', 'multimedia_videos', name='multimedia_videos'),
#     url(r'^privado/multimedia_videos_tag/(?P<tags>\w+)/$', 'multimedia_videos_tag', name='multimedia_videos_tag'),
#     url(r'^privado/multimedia_videos_sel/(?P<video>\w+)/$', 'multimedia_videos_sel', name='multimedia_videos_sel'),
#     url(r'^privado/multimedia_audios/$', 'multimedia_audios', name='multimedia_audios'),
#     url(r'^privado/multimedia_audios_tag/(?P<tags>\w+)/$', 'multimedia_audios_tag', name='multimedia_audios_tag'),    
#     url(r'^aporte/editar/(?P<aporte_id>\d+)/$', 'editar_aporte', name='editar-aporte'),
#     url(r'^aporte/borrar/(?P<id>\d+)/$', 'borrar_aporte', name='borrar-aporte'),
#     url(r'^comentario/editar/(?P<comen_id>\d+)/$', 'editar_comentario', name='editar-comentario'),
#     url(r'^comentario/borrar/(?P<id>\d+)/$', 'borrar_comentario', name='borrar-comentarios'),
]