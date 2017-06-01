from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.portfolioIndex, name="index"),
	url(r'^addportfolio/$', views.addPortfolio, name="addportfolio"),
	url(r'^category/(?P<pk>[0-9]+)/$', views.portfolioCatDetail, name="catdetail"),
	url(r'^(?P<slug>[0-9]+)/$', views.portfolioDetail, name='detail'),
]