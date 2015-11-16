from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.index, name='login'),
    url(r'^logout/$', views.logging_out, name='logging_out'),
    url(r'^catalogue/$', views.catalogue, name='catalogue'),
    url(r'^register/$', views.register, name='register'),
    url(r'^reg_success/$', views.reg_success, name='reg_success'),
    url(r'^rate/$', views.rate, name='rate'),
    url(r'^remove_from_wardrobe/$', views.remove_from_wardrobe, name='remove'),
    url(r'^add_to_wardrobe/$', views.add_to_wardrobe, name='add'),
    url(r'^wardrobe/$', views.wardrobe, name='wardrobe'),
    #url(r'^$', views.catalogue, name='catalogue'),
    url(r'^catalogue/(?P<category_name>\D+)/$', views.catalogue, name='catalogue_category'),
]