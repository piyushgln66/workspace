from django.conf.urls import patterns, url
from connections import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^profile/$', views.profile, name='profile'),
	url(r'^register/$', views.register, name='register'),
	url(r'^login/$', views.user_login, name='user_login'),
	url(r'^logout/$', views.user_logout, name='user_logout'),
	url(r'^fetch/$', views.fetch_content, name='fetch_content'),
	url(r'^upload/$', views.upload, name='upload'),
)