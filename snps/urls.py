from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^search/$', views.search, name='search'),
    url(r'^search_interval/$', views.search_interval, name='search_interval'),
    url(r'^phenotype_list/$', views.phenotype_list, name='phenotype_list'),
    url(r'^search_phenotype/$', views.search_phenotype, name='search_phenotype'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
]
