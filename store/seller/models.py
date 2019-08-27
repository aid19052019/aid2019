from django.db import models

# Create your models here.
# file: seller/models.py
# 店主信息
class Shopkeeper(models.Model):
    card_type =  models.CharField(max_length=10,verbose_name='证件类型')
    card_num = models.CharField(max_length=32,verbose_name='证件号码')
    pic = models.BinaryField(verbose_name='证件照片')
    validity_date = models.DateField(verbose_name='证件有效期')
    upd_time = models.DateTimeField(auto_now=True,verbose_name='更新时间')
    create_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')


# 店铺信息
class Store(models.Model):
    open_date = models.DateField(verbose_name='开店日期')
    level = models.CharField(max_length=16,verbose_name='店铺等级')
    address = models.CharField(max_length=254,verbose_name='店铺地址')
    store_type = models.CharField(max_length=16,verbose_name='店铺分类')
    upd_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    shopkeeper = models.OneToOneField(Shopkeeper)  # 店主-店铺一对一

# 商品
class Goods(models.Model):
    color = models.CharField(max_length=10,verbose_name='颜色')
    size = models.CharField(max_length=10,verbose_name='尺寸')
    price = models.DecimalField(max_digits=8,decimal_places=2,verbose_name='价格')


# 商家宝贝
class ShopGoods(models.Model):
    goods_title = models.CharField(max_length=100,verbose_name='商品标题')
    goods_type = models.CharField(max_length=16,verbose_name='商品类型')
    upd_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    goods = models.OneToOneField(Goods) # 店铺宝贝-商品  一对一
    store = models.ForeignKey(Store)  # 店铺-店铺宝贝  一对多


