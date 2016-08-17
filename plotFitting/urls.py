from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'sloppyCellReports', views.sloppyCellReports, name='sloppyCellReports'),
    url(r'P2011_load', views.P2011_load, name='P2011_load'),
    url(r'plotFitting', views.plotFitting, name='plotFitting'),
    url(r'run_fitting', views.run_fitting, name='run_fitting'),
]