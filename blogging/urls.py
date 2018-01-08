from django.conf.urls import url
from django.contrib import admin
from .views import(
post_list,
post_create,
post_details,
post_update,
post_delete,
)
app_name = 'blogging'
urlpatterns=[
    url(r'^$', post_list, name='allpost'),
    url('create/$', post_create),
    url(r'^(?P<id>\d+)/$', post_details, name='details'),
    url(r'^(?P<id>\d+)/edit/$', post_update, name='update'),
    url(r'^(?P<id>\d+)/delete/$', post_delete),
]