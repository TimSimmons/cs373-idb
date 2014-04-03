from django.conf.urls import patterns, include, url

from django.contrib import admin
import idb.api as api
from idb.views import home, player, team, year, team_abbr, players, teams, years
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', home),
    url(r'^players/$', players),
    url(r'^teams/$', teams),
    url(r'^years/$', years),
    url(r'^players/(\d*)/$', player),
    url(r'^teams/(\d*)/$', team),
    url(r'^teams/([A-Za-z]{3})/$', team_abbr),
    url(r'^years/(\d{4})/$', year),
    url(r'^admin/', include(admin.site.urls)),
        
    url(r'^api/players/(\d{2})/years/(\d{2})$', api.player_year),
    url(r'^api/players/(\d{2})/years$', api.player_years),
    
    url(r'^api/players/(\d{2})/$', api.player),
    url(r'^api/players/$', api.players),
    
    url(r'^api/teams/(\d{2})/years/(\d{2})$', api.team_year),
    url(r'^api/teams/(\d{2})/years$', api.team_years),
    
    url(r'^api/teams/(\d{2})/$', api.team),
    url(r'^api/teams/$', api.teams),
   
    url(r'^api/years/(\d{4})/$', api.year),
)

