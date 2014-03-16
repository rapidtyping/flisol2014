from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('flisol.apps.page.views',
	url(r'^$', 'index_view', name = 'vista_principal'),
)