from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path('^$', views.Home.as_view(), name="home"),
    re_path('^result/$', views.result, name="result"),
]


app_name = 'recips'
