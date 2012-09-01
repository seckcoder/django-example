from django.conf.urls import patterns, include, url
urlpatterns = patterns('blog.views',
                       url(r'^$', 'posts', name='posts'),
                       url(r'^js$', 'test_js'),
                       url(r'^author/(\d+)/$', 'author_detail', name='author_detail_view'))
