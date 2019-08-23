from django.conf.urls import url
from products import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^product/(?P<product_id>\w+)/$', views.product, name="product"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
