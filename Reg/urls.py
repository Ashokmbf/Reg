"""Reg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.contrib import admin



urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
    #url(r'^$', 'django_social_app.views.login'),
    url(r'^',include('polls.urls', namespace="polls")),
    #url('^oauth/', include('social.apps.django_app.urls', namespace='social')),
    #url('', include('social.apps.django_app.urls', namespace='social')),
    #url(r'^oauth/', include('social_django.urls', namespace='social')),
    
    url(r'^signup/',include('polls.urls', namespace="polls")),
    url(r'^login/',include('polls.urls', namespace="polls")),
    url(r'^forgot/',include('password_reset.urls', namespace="polls")),
    url(r'^reset/',include('polls.urls', namespace="polls")),
    url(r'^userpage/',include('polls.urls', namespace="polls")),
    url(r'^logout/',include('polls.urls', namespace="polls")),
    url(r'^loginfb/',include('polls.urls', namespace="polls")),
    


    #include('password_reset.urls')
]

 