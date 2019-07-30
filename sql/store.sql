create database store charset=utf8;

#订单表
create table orders(
    order_id int auto_increment primary key,
    order_no varchar(40),#订单号
    user_id int,#买家ID
    goods_money decimal(10,2),#商品总金额
    express_fee decimal(10,2),#快递费
    all_money decimal(10,2), #订单总金额
    actual_money decimal(10,2),#实际支付金额
    status char(1),#订单状态 0等待付款/1交易已完成/2交易失效
    adress varchar2(5),#订单地址,来源：用户地址表的ID
    exist_flag boolean,#订单是否被删除，没有删除为 True
    create_time timestamp, #订单创建时间
    close_time datetime, # 订单关闭时间
    remark varchar(1000) #备注
);

#订单明细表
create table order_list(
    list_id int auto_increment primary key,
    order_id int,#订单id,来源：order.order_id
    seller_id int,#卖家id,来源：用户表
    goods_id int,#商品id,来源：商品明细表
    price decimal(10,2),#单价
    amount int,#数量
    all_money decimal(10,2) #总金额
);

#购物车
create table shopping_trolley(
    id int auto_increment primary key
);

#收藏夹_商品
create table favorite_goods(
    id int int auto_increment primary key,
    user_id int ,#买家ID,
    goods_id int,#商品id,来源：商品明细表
    create_time timestamp 
)

#收藏夹_店铺
create table favorite_shop(
    id int int auto_increment primary key,
    user_id int ,#买家ID,
    shop_id int,#店铺id,来源：店铺表
    create_time timestamp 
)
