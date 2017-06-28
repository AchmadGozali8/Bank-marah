"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
#from apps.views import Posts, PostsUpdate
from django.views.generic import TemplateView
from apps.views import CreatePost, UpdatePost, DeletePost, Home
from django.contrib.auth import views as auth_views
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
#    url(r'^', include('apps.api.urls')),
    url(r'^$', Home, name='Home'),
    url(r'^home/$', TemplateView.as_view(template_name='home.html')),
    url(r'^post/$', Home),
    url(r'^create/$', CreatePost),
    url(r'^admin/', admin.site.urls),
#    url(r'^update/(?P<pk>\d+)/$', PostsUpdate.as_view()),
    url(r'^login/$', auth_views.login, {'template_name':'login.html'},
        name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page':'/login/'}),
    url(r'^update/(?P<pk>\d+)/$', UpdatePost, name='update'),
    url(r'^deleted/(?P<pk>\d+)/$', DeletePost, name='delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
