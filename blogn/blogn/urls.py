"""blogn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
import blogn.posts.views
import blogn.sitepages.views
import blogn.accounts.views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', blogn.posts.views.home, name='home'),
    url(r'^', include('blogn.posts.urls')),
    url(r'^about/', blogn.sitepages.views.about, name='about'),
    url(r'^signup/', blogn.accounts.views.signup, name='signup'),
    url(r'^signin/', blogn.accounts.views.signin, name='signin'),
    url(r'^logout_user/', blogn.accounts.views.logout_user, name='logout_user'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
