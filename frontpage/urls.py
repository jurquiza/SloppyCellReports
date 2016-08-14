from django.conf.urls import include, url
from . import views

urlpatterns = [
    
    url(r'^$', views.main_page, name='main_page'),
    url(r'about/', views.about, name='about'),

]