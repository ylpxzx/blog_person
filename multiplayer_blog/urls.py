"""multiplayer_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import xadmin
from django.contrib import admin
#from django.urls import path
from django.conf.urls import url
#from blog.views import post_list,post_detail
from django.urls import re_path
from django.views.static import serve
from multiplayer_blog.settings.base import MEDIA_ROOT
from blog.views import (
IndexView,CategoryView,TagView,
PostDetailView,SearchView,AuthorView
)
from config.views import LinkListView
from comment.views import CommentView
from django.contrib.sitemaps import views as sitemap_views
from blog.rss import LatestPostFeed
from blog.sitemap import PostSitemap
from .autocomplete import CategoryAutocomplete,TagAutocomplete
from django.conf import settings
from django.conf.urls import url,include
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from blog.apis import PostViewSet,CategoryViewSet
from rest_framework.documentation import include_docs_urls
from django.views.decorators.cache import cache_page
#采用django-rest-framework提供的router更好的生成URL
router=DefaultRouter()
router.register(r'post',PostViewSet,base_name='api-post')

router.register(r'category',CategoryViewSet,base_name='api-category')

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^category/(?P<category_id>\d+)/$', CategoryView.as_view(), name='category-list'),
    url(r'^tag/(?P<tag_id>\d+)/$', TagView.as_view(), name='tag-list'),
    url(r'^search/$', SearchView.as_view(), name='search'),
    url(r'^comment/$', CommentView.as_view(), name='comment'),
    url(r'^author/(?P<owner_id>\d+)/$', AuthorView.as_view(), name='author'),
    url(r'^post/(?P<post_id>\d+).html$', PostDetailView.as_view(), name='post-detail'),
    url(r'^links/$', LinkListView.as_view(), name='links'),
    url(r'^admin/',xadmin.site.urls,name='xadmin'),
    url(r'^rss|feed/',LatestPostFeed(),name='rss'),
    url(r'^sitemap\.xml$', cache_page(60 * 20, key_prefix='sitemap_cache_')(sitemap_views.sitemap), {'sitemaps': {'posts': PostSitemap}}),
    url(r'^category-autocomplete/$',CategoryAutocomplete.as_view(),name='category-autocomplete'),
    url(r'^tag-autocomplete/$',TagAutocomplete.as_view(),name='tag-autocomplete'),
    url(r'^ckeditor/',include('ckeditor_uploader.urls')),
    url(r'^api/',include(router.urls)),
    re_path('media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),
    url(r'^api/docs/',include_docs_urls(title='gulang_blog apis')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



#只有在DEBUG模式下才加载debug_toolbar模块
'''if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns'''