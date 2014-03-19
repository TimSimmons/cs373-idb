from django.conf.urls import patterns, include, url

from django.contrib import admin
from idb.views import home, player, team, year
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'idb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', home),
    url(r'^players/(\d{2})/$', player),
    url(r'^teams/(\d{2})/$', team),
    url(r'^years/(\d{4})/$', year),
    url(r'^admin/', include(admin.site.urls)),
)

