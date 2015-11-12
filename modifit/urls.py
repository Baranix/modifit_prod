from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.index, name='index'),
    url(r'^logout/$', views.logging_out, name='logging_out'),
    url(r'^home/$', views.home, name='home'),
    url(r'^register/$', views.register, name='register'),
    url(r'^reg_success/$', views.reg_success, name='reg_success'),
    url(r'^rate/$', views.rate, name='rate'),
    url(r'^wardrobe/$', views.wardrobe, name='wardrobe'),
    #url(r'^$', views.home, name='home'),
    #url(r'^(?P<wardrobe_id>[0-9]+)/$', views.wardrobe, name='wardrobe'),
]