from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path('^$', views.Home.as_view(), name="home"),
    re_path('^result/$', views.result, name="result"),
    re_path('^result/(?P<page>\d+)$', views.result, name="result"),
    re_path('^detail/(?P<pk>\d+)$', views.Detail.as_view(), name="detail"),
    re_path('^create/$', views.create, name="create"),
]

app_name = 'recips'