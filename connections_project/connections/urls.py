from django.conf.urls import patterns, url
from connections import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
)