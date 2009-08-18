from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    url('^(?P<page>)$', views.index, name="home"),
]


app_name = 'recips'
