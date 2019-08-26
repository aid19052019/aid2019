from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^order$', views.list),
    url(r'^settlement$', views.settlement),  # 结算 order/settlement
    url(r'^shopping_car$', views.shopping_car),  # 结算 order/settlement
]
