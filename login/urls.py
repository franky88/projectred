from django.conf.urls import include, url
from . import views

app_name = 'login'
urlpatterns = [
    url(r'^$', views.userLogin, name='index'),
    url(r'^adduser/$', views.userAdd, name="adduser"),
    url(r'^logout/$', views.userLogout, name='logout'),
]