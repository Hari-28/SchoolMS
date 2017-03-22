from django.conf.urls import url
from .import views

urlpatterns = [
    #/polls/
    url(r'^$', views.index, name='index'),

    #/polls/71/
    url(r'^[0-9]+/$', views.detail, name='index'),
    url(r'^registar.html/$', views.reg, name='reg'),
    url(r'^correspondent.html/$', views.cor, name='cor'),
    url(r'^headregistar.html/$', views.hreg, name='hreg'),
    url(r'^correspondent.html/c_addstudent.html/$', views.caddstud, name='caddstud'),
    url(r'^correspondent.html/c_addregistar.html/$', views.caddreg, name='caddreg'),
    url(r'^correspondent.html/c_addstaff.html/$', views.caddstaff, name='caddstaff'),
    url(r'^correspondent.html/c_request.html/$', views.creq, name='creq'),
]
