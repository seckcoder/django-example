from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
                       url(r'^polls/', include('polls.urls')),
                       url(r'^blog/', include('blog.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       )