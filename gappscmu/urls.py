from django.conf.urls import patterns, url

urlpatterns = patterns('gappscmu.views',
    url(r'^$', 'home'),
    url(r'^logout/$', 'logout'),
)
