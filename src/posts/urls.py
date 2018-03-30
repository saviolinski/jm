from django.conf.urls import url
from django.contrib import admin

from .views import (
		posts_list,
		posts_create,
		posts_delete,
		posts_update,
		posts_detail,
		index
	)


urlpatterns = [
	url(r'^$', index, name="list"),
    url(r'^artykuly/$', posts_list, name="list"),
    url(r'^create/$', posts_create),
    url(r'^(?P<slug>[\w-]+)/delete/$', posts_delete, name="delete"),
    url(r'^(?P<slug>[\w-]+)/edit/$', posts_update, name="update"),
    url(r'^(?P<slug>[\w-]+)/$', posts_detail, name="detail"),
]