from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^goods_store',views.goods_store_view),
]