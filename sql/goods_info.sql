create database goods charset=utf8;

CREATE TABLE goods_info (
  id int(11) NOT NULL AUTO_INCREMENT,
  title varchar(32) NOT NULL,# 商品标题
  class1 enum(男装,女装,童装) NOT NULL,# 一级类目
  class2 enum(夹克,上衣,裤子,裙子,鞋子,毛衣,衬衣,风衣,针织衫,西装,棉袄,配饰,其他) NOT NULL,# 二级类目
  class_size set(XS,S,M,L,XL,XXL) NOT NULL,# 商品尺码
  class_color set(红色,橙色,黄色,绿色,青色,蓝色,紫色,灰色,粉色,黑色,白色,棕色) NOT NULL,# 商品颜色
  price decimal(6,2) NOT NULL,# 商品价格
  storage decimal(6,0) NOT NULL,# 商品库存
  sales_volume decimal(8,0) DEFAULT NULL,# 商品销量
  class_fabric varchar(6) DEFAULT NULL,# 商品材质
  class_style set(校园,商务,休闲,运动,百搭,通勤,甜美,小清新) DEFAULT NULL,#商品风格
  class_type set(加大,宽松,标准,修身) DEFAULT NULL,# 商品版型
  class_season set(春季,夏季,秋季,冬季) DEFAULT NULL,# 适应季节
  class_brand varchar(10) DEFAULT NULL,# 商品品牌
  updata time NOT NULL,# 更新时间
  note text,# 备注
  PRIMARY KEY (id) # 外键 商家ID
)

