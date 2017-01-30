"""Calculus URL Configuration

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
from django.conf.urls import url
from .views import company, year, version

urlpatterns = [
    # Companies
    url(r'^$', company.CompanyView.as_view(), name='company_index'),

    # Years
    url(r'^(?P<company_id>\d+)/$', year.YearListView.as_view(), name='year_index'),
    url(r'^(?P<company_id>\d+)/(?P<year_id>\d+)/detail$', year.YearDetailView.as_view(), name='year_detail'),
    
    #Versionen     
    url(r'^(?P<company_id>\d+)/(?P<year_id>\d+)/$', version.VersionListView.as_view(), name='version_index'),
]


