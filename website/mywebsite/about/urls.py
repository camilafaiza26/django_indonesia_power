from django.conf.urls import url

from . import views
from blog.views import *

urlpatterns = [
    url(r'^recent/$', views.recent),
    url(r'^$', views.index, name="index"),
    url(r'^inputsolver', views.inputsolver, name="inputsolver"),
    url(r'^hasiloptimalisasisolver', views.hasiloptimalisasisolver, name="hasiloptimalisasi"),
    url(r'^resumesolver', views.resumesolver),
    #url(r'^updaterencanakebutuhan', views.updaterencanakebutuhan, name="updaterencanakebutuhan"),
    url(r'^tambahmastersolver', views.tambahmastersolver),
    url(r'^hapusmastersolver/(?P<pk>\d+)$', views.hapusmastersolver),
    url(r'^editmastersolver/(?P<pk>\d+)$', views.editmastersolver),
    url(r'^editmastersolver/updatemastersolver/(?P<pk>\d+)$', views.updatemastersolver),
    url(r'^login/$', views.loginView, name="login"),

]
