from django.conf.urls import patterns, include, url
from django.contrib import admin

from siteapp.views import HomeView

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    # url(r'^blog/', include('blog.urls')),


	url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
	
	# url(r'^accounts/login$', 'django_cas.views.login'),
 #    url(r'^logout$', 'django_cas.views.logout'),
    
    url(r'^admin/', include(admin.site.urls)),
)
