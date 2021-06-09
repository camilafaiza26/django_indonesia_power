from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
    url(r'^recent/$', views.recent),
    url(r'^$', views.index),
    url(r'^tambah/tambahrekap', views.tambahrekap, name='tambahrekap'),
    url(r'^tambah', views.tambah, name='tambah'),
    url(r'^hapusrekap/(?P<pk>\d+)$', views.hapusrekap),
    url(r'^editrekap/(?P<pk>\d+)$', views.editrekap),
    url(r'^editrekap/updaterekap/(?P<pk>\d+)$', views.updaterekap),
]
