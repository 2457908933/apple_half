"""apple_blog URL Configuration

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
from blog import views


urlpatterns = [

    url(r'^(?P<article_type_id>\d+)/', views.index),
    url(r'^comment/', views.comment),
    url(r'^poll/', views.poll),
    url("(?P<username>\w+)/article/(?P<condition>category|tag|date)/(?P<para>.*)", views.blog),
    url(r'^(?P<username>\w+)/$', views.blog),
    url(r'^(?P<username>\w+)/(?P<article_id>\d+)/$', views.blog_text),


]