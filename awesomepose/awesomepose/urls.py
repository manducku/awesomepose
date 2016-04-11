"""awesomepose URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings

from users.views import *
from posts.views import *
from posts.api import *
from tags.views import *
from awesomepose.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', PostListView.as_view(), name="home"),
    url(r'^signup/$', SignupView.as_view(), name="sign-up"),

    url(r'', include('social.apps.django_app.urls', namespace='social')),

    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^welcome/$', WelcomeView.as_view(), name="welcome"),
    url(r'^logout/$', LogoutView.as_view(), name="logout"),
    url(r'^profile/(?P<slug>\w+)/$', ProfileListView.as_view(), name="profile"),

    url(r'^posts/$', PostListView.as_view(), name="posts"),
    url(r'^posts/new/$', PostCreateView.as_view(), name="post-new"),
    url(r'^posts/(?P<slug>\w+)/$', PostDetailView.as_view(), name="detail"),
    url(r'^posts/(?P<slug>\w+)/comments/$', PostCommentCreateView.as_view(), name="post-comments"),

    url(r'^api/posts/$', PostListAPIView.as_view(), name="api-posts"),
    url(r'^api/posts/(?P<slug>\w+)/$', PostCommentListAPIView.as_view(), name="api-comment-list"),


    url(r'^explore/tags/(?P<slug>\w+)/$', TagDetailView.as_view(), name="tag-detail"),
    url(r'^summernote/', include('django_summernote.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
