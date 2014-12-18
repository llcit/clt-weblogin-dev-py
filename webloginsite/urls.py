from django.conf.urls import patterns, include, url
from django.contrib import admin

from siteapp.views import HomeView

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^accounts/login$', 'django_cas_ng.views.login'),
    url(r'^accounts/logout$', 'django_cas_ng.views.logout'),
    url(r'^admin/', include(admin.site.urls)),
)
