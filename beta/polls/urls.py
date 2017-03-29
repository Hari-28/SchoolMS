from django.conf.urls import url
from .import views

urlpatterns = [
    #/polls/
    url(r'^$', views.index, name='index'),

    #/polls/71/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='index'),
    url(r'^registar.html/$', views.reg, name='reg'),
    url(r'^correspondent.html/$', views.my_view, name='my_view'),
    url(r'^correspondent.html/$', views.cor, name='cor'),
    url(r'^correspondent/#(?P<side_id>[0-9]+)/$', views.side, name='side'),
    url(r'^headregistar.html/$', views.hreg, name='hreg'),
    url(r'^correspondent.html/c_addstudent.html/$', views.caddstud, name='caddstud'),
    url(r'^correspondent.html/c_addfaculty.html/$', views.caddfac, name='caddfac'),
    url(r'^correspondent.html/c_addregistar.html/$', views.caddreg, name='caddreg'),
    url(r'^correspondent.html/c_addstaff.html/$', views.caddstaff, name='caddstaff'),
    url(r'^correspondent.html/c_request.html/$', views.creq, name='creq'),
    url(r'^correspondent.html/c_approval.html/$', views.capp, name='capp'),
]
