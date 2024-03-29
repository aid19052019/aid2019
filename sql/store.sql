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


# 店主信息
create table shopkeeper(
    id int primary key auto_increment,
    card_type char(10), # 证件类型
    card_num char(32),   # 证件号码
    pic blob,   # 证件照片
    validity_date date, # 证件有效期
    upd_time datetime, # 更新时间
    create_time datetime # 创建时间
);


# 店铺信息
create table store(
    id int primary key auto_increment,
    seller_no int ,  # 商家编码
    open_date  date, # 开店日期
    level varchar(16), # 商铺等级
    address varchar(32), # 店铺地址
    store_type varchar(16), # 店铺分类
    upd_time datetime, # 更新时间
    create_time datetime # 创建时间
);


# 商家宝贝
create table shop_goods(
    id int primary key auto_increment,
    goods_id  int, # 商品id (关联“商品”表)
    goods_title varchar(16), # 商品标题
    goods_type varchar(16),  # 商品类型
    seller_id int, # 商家id (关联“店铺”表)
    upd_time datetime, # 更新时间
    create_time datetime # 创建时间
);


# 历史交易记录
create table buy_history(
    id int primary key auto_increment,
    user_id varchar(16), # 买家id (关联“用户”表)
    seller_id int, # 商家id  (关联“店铺”表)
    goods_id  int, # 商品id (关联“商品”表)
    order_id  int # 订单id (关联“订单”表)
    upd_time datetime, # 更新时间
    create_time datetime # 创建时间
);

#用户信息表
创建 表 users(
	phone_number: TINYINT(44) #手机号    
	email: VARCHAR(128) #邮箱
	user_name: VARCHAR(32) NOT NULL #用户名
	user_password: VARCHAR(128) NOT NULL #密码
	user_id: INT AUTO_INCREMENT PRIMARY KEY #用户id
	head_portrait: TEXT DEFAULT #头像(默认为一张图片具体写法查看一下)
	nickname: VARCHAR(32) DEFAULT #昵称(默认与用户名相同)
	sex: CHAR(16) DEFAULT #性别(要求设置默认值)
	real_name: VARCHAR(32) #真实姓名
	date_of_Birth: INT #出生日期
	residential_address: VARCHAR(1024) #居住地址
	hometown: VARCHAR(128) #家乡
	)
#历史信息:(对接订单表)
创建 表 order_list(
	individual_orders_id: INT AUTO_INCREMENT PRIMARY KEY #个人历史信息id
	user_id #用户id
	store_id #店铺id
	commodity_id #商品id
	unit_purchased_cost #购买单价
	purchase_quantity #购买数量
	total_money #总金额
	)
#收货地址: 
创建 表 shipping_address(
	shipping_address_id: INT AUTO_INCREMENT PRIMARY KEY #收货地址id
	user_id: #用户id
	consignee:VARCHAR(32) #收货人姓名
	area: VARCHAR(32) #所在地区
	province: VARCHAR(30) #省
	city #市
	county #县/区
	detailed address: txet #详细地址
	postcode: INT(24) #邮政编码
	phone_number: TINYINT(44) #手机号码
	)
#收藏夹:(对接店铺信息表)
创建 表 favorite_shop（
	store_id: #店铺id
	store_name: #店铺名称
	需要设置操作:添加/删除
	note: TEXT #备注
	label classification:TEXT #标签分类
	)
