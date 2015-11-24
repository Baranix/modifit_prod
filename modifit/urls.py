from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^login/$', views.index, name='login'),
	url(r'^logout/$', views.logging_out, name='logging_out'),
	url(r'^register/$', views.register, name='register'),
	url(r'^reg_success/$', views.reg_success, name='reg_success'),
	url(r'^rate/$', views.rate, name='rate'),
	url(r'^remove_from_wardrobe/$', views.remove_from_wardrobe, name='remove'),
	url(r'^add_to_wardrobe/$', views.add_to_wardrobe, name='add'),
	url(r'^wardrobe/$', views.wardrobe, name='wardrobe'),
	url(r'^wardrobe/(?P<category_name>\D+)/$', views.wardrobe, name='wardrobe_category'),
	url(r'^catalogue/$', views.catalogue, name='catalogue'),
	url(r'^catalogue/(?P<category_name>\D+)/$', views.catalogue, name='catalogue_category'),
	url(r'^item/(?P<item_id>[0-9]+)/$', views.item, name='item'),
	#url(r'^recommend/$', views.recommend, name='recommend'),
	#url(r'^recommend/(?P<recommender>\D+)/$', views.recommend, name='recommender'),
	url(r'^recommendations/$', views.recommendations, name='recommendations'),
	url(r'^rate_recommendation/$', views.rate_recommendation, name='rate_recommendation'),
]