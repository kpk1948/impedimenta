from django.conf.urls import patterns, url, include

urlpatterns = patterns('mhs.views',
    url(r'^home$', 'home'),
    url(r'^login/$', 'login'),
)