from django.urls import path
from django.conf.urls import url, include
from django.contrib import admin
from . import views
from .views import *
from wkhtmltopdf.views import PDFTemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^about/', include('about.urls')),
    url(r'^master/', include('master.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name="index"),
    #url(r'^$', views.index),
    url(r'^logout/$', logoutView, name="logout"),
	url(r'^login/$', loginView, name="login"),
    url(r'^grading/$', views.grading, name="grading"),
    url(r'^grading/detailgrading/(?P<pk>\d+)$', views.detailgrading, name="detailgrading"),
    url(r'^grading/detailgrading/printnilai/(?P<pk>\d+)$', views.printnilai, name="printnilai"),
    url(r'^grading/konfirgrading', views.konfirgrading, name='konfirgrading'),
    url(r'^grading/prosesgrading', views.prosesgrading, name='prosesgrading'),
    url(r'^grading/detailgrading/printnilai/$', views.printnilai, name="printnilai"),
    #url(r'^inputgrading', views.inputgrading, name='inputgrading'),
]
'''
urlpatterns = patterns('app.views',
    url(r'^dashboard$', 'dashboard', name='dashboard'),
    url(r'^dashboard/(?P<date>[\d]{8})/$', 'dashboard', name='dashboard'),
    url(r'^dashboard/(?P<account_uid>[\da-zA-Z-]{36})/$', 'dashboard', name='dashboard'),
    url(r'^dashboard/(?P<date>[\d]{8})/(?P<account_uid>[\da-z-]{36})/$', 'dashboard', name='dashboard'),
)
'''
