from django.db import models


# Create your models here.

class Order(models.Model):
    order_id = models.AutoField(primary_key=True, verbose_name="订单ID")
    order_no = models.CharField(unique=True, max_length=40, verbose_name="订单号")
    user_id = models.IntegerField(verbose_name="买家ID")
    goods_money = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="商品总金额", default=9999999.0)
    express_fee = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="快递费", default=0.0)
    all_money = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="订单总金额")
    actual_money = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="实际支付金额")
    status = models.IntegerField(verbose_name="订单状态 0等待付款/1交易已完成/2交易失效", default=0)
    adress_id = models.IntegerField(verbose_name="订单地址,来源：用户地址表的ID")
    exist_flag = models.IntegerField(default=0, verbose_name="订单是否被删除,0表示没有删除 1表示删除")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="订单创建时间")
    close_time = models.DateTimeField(null=True, blank=True, verbose_name="订单关闭时间")
    remark = models.CharField(null=True, blank=True, max_length=1000, verbose_name="备注")


# 订单明细表
class OrderList(models.Model):
    list_id = models.AutoField(verbose_name="订单明细ID", primary_key=True)
    order_id = models.ForeignKey(Order, null=True, verbose_name="订单id")
    seller_id = models.IntegerField(verbose_name="卖家id")
    goods_id = models.IntegerField(verbose_name="商品id")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="单价")
    amount = models.IntegerField(default=0, verbose_name="数量")
    all_money = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="总金额")


# 购物车
class ShoppingCar(models.Model):
    shopping_car_id = models.AutoField(verbose_name="购物车ID", primary_key=True)
    user_id = models.IntegerField(verbose_name="买家ID")
    goods_id = models.IntegerField(verbose_name="商品id")
    amount = models.IntegerField(default=0, verbose_name="数量")
    if_order = models.IntegerField(verbose_name="是否生成订单")  # 是否生成订单(0.没有生成订单 1.已经生产订单)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="单价")
