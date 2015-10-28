from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.index, name='index'),
    url(r'^logout/$', views.logging_out, name='logging_out'),
    url(r'^home/$', views.home, name='home'),
    #url(r'^$', views.home, name='home'),
    url(r'^(?P<wardrobe_id>[0-9]+)/$', views.wardrobe, name='wardrobe'),
]