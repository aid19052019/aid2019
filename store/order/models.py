from django.db import models


# Create your models here.

class Order(models.Model):
    order_id = models.AutoField(primary_key=True,verbose_name="订单ID")
    order_no = models.CharField(unique=True,max_length=40, verbose_name="订单号")
    user_id = models.IntegerField(verbose_name="买家ID")
    goods_money = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="商品总金额")
    express_fee = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="快递费")
    all_money = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="订单总金额")
    actual_money = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="实际支付金额")
    status = models.IntegerField(verbose_name="订单状态 0等待付款/1交易已完成/2交易失效")
    adress_id = models.IntegerField(verbose_name="订单地址,来源：用户地址表的ID")
    exist_flag = models.IntegerField(default=0, verbose_name="订单是否被删除,0表示没有删除 1表示删除")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="订单创建时间")
    close_time = models.DateTimeField(verbose_name="订单关闭时间")
    remark = models.CharField(max_length=1000, verbose_name="备注")


# 订单明细表
class OrderList(models.Model):
    list_id = models.AutoField(verbose_name="订单明细ID", primary_key=True)
    order_id = models.IntegerField(verbose_name="订单id,来源：order.order_id")
    seller_id = models.IntegerField(verbose_name="卖家id,来源：用户表")
    goods_id = models.IntegerField(verbose_name="商品id,来源：商品明细表")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="单价")
    amount = models.IntegerField(default=0, verbose_name="数量")
    all_money = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="总金额")
