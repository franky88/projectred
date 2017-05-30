from django.conf.urls import url
from . import views

app_name="reduser"
urlpatterns = [
	url(r'^$', views.portfolioUser, name="userindex"),
	url(r'^user/(?P<pk>[0-9]+)/$', views.portfolioUserDetail, name="userdetail"),
]