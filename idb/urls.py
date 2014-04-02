from django.conf.urls import patterns, include, url

from django.contrib import admin
from idb.views import home, player, team, year, player_model
from idb.api import api_player
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'idb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', home),
    url(r'^players/(\d{2})/$', player),
    url(r'^players_model/(\d{1})/$', player_model),
    url(r'^teams/([A-Za-z]{3})/$', team),
    url(r'^years/(\d{4})/$', year),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/players/(\d{2})/$', api_player)
)

