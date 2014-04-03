from django.conf.urls import patterns, include, url

from django.contrib import admin
from idb.views import home, player, team, year, team_abbr
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', home),
    url(r'^players/(\d*)/$', player),
    url(r'^teams/(\d*)/$', team),
    url(r'^teams/([A-Za-z]{3})/$', team_abbr),
    url(r'^years/(\d{4})/$', year),
    url(r'^admin/', include(admin.site.urls)),
)

