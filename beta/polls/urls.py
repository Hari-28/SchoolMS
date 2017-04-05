from django.conf.urls import url
from .import views

urlpatterns = [
    #/polls/
    url(r'^$', views.index, name='index'),
    url(r'^#', views.login, name='login'),



    url(r'^correspondent.html/$', views.cor, name='cor'),
    url(r'^c_addstudent.html/$', views.caddstud, name='caddstud'),
    url(r'^c_addfaculty.html/$', views.caddfac, name='caddfac'),
    url(r'^c_addregistar.html/$', views.caddreg, name='caddreg'),
    url(r'^c_addstaff.html/$', views.caddstaff, name='caddstaff'),
    url(r'^c_request.html/$', views.creq, name='creq'),
    url(r'^c_approval.html/$', views.capp, name='capp'),



    url(r'^headregistar.html/$', views.hreg, name='hreg'),
    url(r'^h_addstudent.html/$', views.haddstud, name='haddstud'),
    url(r'^h_addfaculty.html/$', views.haddfac, name='haddfac'),
    url(r'^h_addstaff.html/$', views.haddstaff, name='haddstaff'),
    url(r'^h_request.html/$', views.hreq, name='hreq'),






    url(r'^registar.html/$', views.reg, name='reg'),
]
