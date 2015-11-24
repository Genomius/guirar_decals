from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
import settings


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^catalog/', 'catalog.views.catalog', name='catalog'),
    url(r'^cart/', 'cart.views.cart', name='cart'),
    url(r'^$', 'project.views.home', name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

