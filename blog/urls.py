from django.conf.urls import re_path
from django.urls import path
from . import views


urlpatterns = [
    re_path(r'^$', views.show),
    re_path(r'^(?P<username>\w+)/$', views.username),
    path('<slug:title>/<int:section>/', views.section),
]