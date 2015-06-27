from django.conf.urls import patterns, include, url
from django.contrib import admin

from siteapp.views import HomeView

urlpatterns = patterns(
    '',
    url(r'^$', HomeView.as_view(), name='home'),

    # CAS AUTHENTICATION
    url(r'^accounts/login/$', 'django_cas.views.login', name='login'),
    url(r'^logout/$', 'django_cas.views.logout', name='logout'),

    # DJANGO AUTHENTICATION
    #   url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
    #   url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),

    url(r'^admin/', include(admin.site.urls)),
)
