import django

print(django.get_version())
# class OrderModel:
#     def __init__(self):
#         order_id
#         order_no
#         user_id
#         goods_money   # 商品总金额
#         express_fee   # 快递费
#         all_money     # 订单总金额
#         actual_money  # 实际支付金额
#         status   # 订单状态 0等待付款/1交易已完成/2交易失效
#         adress   # 订单地址,来源：用户地址表的ID
#         exist_flag   #订单是否被删除，没有删除为 True
#         create_time  #订单创建时间
#         close_time # 订单关闭时间
#         remark # 备注