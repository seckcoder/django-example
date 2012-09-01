from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
                       url(r'^polls/', include('polls.urls')),
                       url(r'^blog/', include('blog.urls')),
                       url(r'^post/(?P<title>[a-zA-Z0-9_\-]+)[/]{0,1}$',
                           'blog.views.post', name='post_view'),
                       url(r'^admin/', include(admin.site.urls)),
                       )
