from django.contrib import admin
from . import models


# Register your models here.

class OrderManage(admin.ModelAdmin):
    list_display = ['order_id',
                    'order_no',
                    'user_id',
                    'goods_money',
                    'express_fee',
                    'all_money',
                    'actual_money',
                    'status',
                    'adress_id',
                    'exist_flag',
                    'create_time',
                    'close_time',
                    'remark']


class OrderListManage(admin.ModelAdmin):
    list_display = ['list_id',
                    'order_id',
                    'seller_id',
                    'goods_id',
                    'price',
                    'amount',
                    'all_money']


admin.site.register(models.Order, OrderManage)
admin.site.register(models.OrderList, OrderListManage)
