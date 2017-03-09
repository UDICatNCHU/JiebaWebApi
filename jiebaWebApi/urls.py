# -*- coding: utf-8 -*-
from django.conf.urls import url
from jiebaWebApi import views
urlpatterns = [
	url(r'^cut$', views.cut),
	url(r'^pos$', views.pos),
]
