from django.conf.urls import patterns, url
import views

urlpatterns = patterns(
    'catalog.views',
    url(r'^$/', views.catalog, name='catalog'),
    #url(r'^(?P<product_slug>[a-zA-Z0-9-_.]+)/$', views.product, name='product'),
)