from django.conf.urls import patterns, url
import views

urlpatterns = patterns(
    'cart.views',
    url(r'^$/', views.cart, name='cart'),
)