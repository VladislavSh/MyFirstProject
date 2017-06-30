from django.conf.urls import url
from . import views

app_name = 'metal'

urlpatterns = [
    # /metal/
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    # /metal/<pk of album>
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /metal/album/add
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),

    # /metal/album/3
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),

    # /metal/album/3/delete
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),

]