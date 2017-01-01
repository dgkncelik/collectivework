"""collectivework URL Configuration

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
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^messages/', include('postman.urls', namespace='postman', app_name='postman')),
    url(r'^ticket/', include('ticket.urls')),
    url(r'^logout/$', 'collectivework.views.logout', name='logout'),
    url(r'^site_rules/$', 'collectivework.views.site_rules', name='site_rules'),
    url(r'^help/$', 'collectivework.views.help', name='help'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^$', 'collectivework.views.login', name='login'),
]
