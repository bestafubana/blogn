from django.conf.urls import url
import blogn.posts.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # url(r'^/(?P<post_id>[0-9]+)/$', blogn.posts.views.post_single, name='postsingle'),
    url(r'^post/(?P<slug>[\w_-]+)/$', blogn.posts.views.post_single, name='postsingle'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
