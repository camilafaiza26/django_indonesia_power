from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^tambahpemasok', views.tambahpemasok),
    url(r'^tambahpltu', views.tambahpltu),
    url(r'^tambahsumbertambang', views.tambahsumbertambang),
    url(r'^hapuspemasok/(?P<pk>\d+)$', views.hapuspemasok),
    url(r'^hapuspltu/(?P<pk>\d+)$', views.hapuspltu),
    url(r'^hapussumbertambang/(?P<pk>[\w\-]+)$', views.hapussumbertambang),
    url(r'^editpemasok/(?P<pk>\d+)$', views.editpemasok),
    url(r'^editpemasok/updatepemasok/(?P<pk>\d+)$', views.updatepemasok),
    url(r'^editpltu/(?P<pk>\d+)$', views.editpltu),
    url(r'^editpltu/updatepltu/(?P<pk>\d+)$', views.updatepltu),
    url(r'^editsumbertambang/(?P<pk>\d+)$', views.editsumbertambang),
    url(r'^editsumbertambang/updatesumbertambang/(?P<pk>\d+)$', views.updatesumbertambang),
    url(r'^editmasterwaktu/(?P<pk>\d+)$', views.editmasterwaktu),
    url(r'^editmasterwaktu/updatemasterwaktu/(?P<pk>\d+)$', views.updatemasterwaktu),
    url(r'^tambahwaktu', views.tambahwaktu),
    url(r'^hapuswaktu/(?P<pk>[\w\-]+)$', views.hapuswaktu),

]
