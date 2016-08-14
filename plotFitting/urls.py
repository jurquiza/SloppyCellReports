from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'', views.plotFitting, name='plotFitting'),
    url(r'^/P2011_load/$', views.P2011_load, name='P2011_load'),
]