from django.views.generic import TemplateView
from django.urls import re_path


from . import views

urlpatterns = [
    re_path('^$', views.connexion, name="connexion"),
    re_path('^create-user/$', views.create_user, name="create"),
    re_path('^connexion/$', views.connexion, name="connexion"),
    re_path('^deconnexion/$', views.deconnexion, name="deconnexion"),
]

app_name="users"