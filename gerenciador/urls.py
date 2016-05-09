"""gerenciador URL Configuration

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
from django.conf.urls import *
#from django.conf.urls import include, url
#from django.contrib import admin
""" 
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
]
"""
urlpatterns = patterns('',
    # Example:
    # (r'^gerenciador/', include('gerenciador.foo.urls')),
    (r'^$', 'agenda.views.index'),
    (r'^adiciona/$', 'agenda.views.adiciona'),
    (r'^item/(?P<nr_item>\d+)/$', 'agenda.views.item'),
    (r'^remove/(?P<nr_item>\d+)/$', 'agenda.views.remove'),
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
