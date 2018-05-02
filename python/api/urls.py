from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from JobCaravan import settings


urlpatterns = {
    path('', views.index, name='index'),
    path('map', views.map),
    path('table',views.table)
}

urlpatterns = format_suffix_patterns(urlpatterns)
