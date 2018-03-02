from django.conf.urls import url
from . import views

app_name = 'music'

# url can perform some logic
urlpatterns = [
    # /music/
    # url(r'^$', views.index, name='index'),
    # go to views and find function index
    url(r'^$', views.IndexView.as_view(), name='index'),


    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    # /music/<album_id>/
    # url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
    # ?P<> say that this is a variable [0-9] digit + any following integer
    url(r'^(?P<pk>[0-9]+)/$', views.DetailsViev.as_view(), name='detail'),

    # /music/<album_id>/favorite/
    # url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite')

    # /music/album/add/
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),

    # /music/album/2/
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),

    # /music/album/2/delete/
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),

    # /music/album/2/favorite/
    url(r'album/(?P<pk>[0-9]+)/favorite/$', views.AlbumFavorite.as_view(), name='album-favorite'),
]
