from django.shortcuts import render
from . import models
from . import order


# Create your views here.
def list(request):
    # user_id = request.GET.get("user_id")
    # order = models.Order.objects.all(user_id = user_id)
    # return render(request,"/order/order_list.html",locals())
    return render(request, "order/order.html")


# 获取商家ID
def get_seller_id():
    pass


def settlement(request):
    if request.method == "POST":
        shopping_car_id_list = request.POST.getlist("shopping_car_id_list")
        order_list = models.OrderList()
        order = models.Order()
        order.order_no = order.get_order_no(shopping_car_id_list[0])
        user_id = request.POST.get("user_id")
        for shopping_car_id in shopping_car_id_list:
            shopping_car_info = order.get_shopping_car(shopping_car_id)
            goods_info = get_seller_id(shopping_car_id_list.goods_id)
            # 从购物车取数量

            # order_l.order_id = 空着
            order_list.seller_id = goods_info.seller_id
            order_list.goods_id = goods_info.goods_id
            order_list.price = goods_info.price
            order_list.amount = shopping_car_info.amount
            order_list.all_money = order_list.amount * order_list.price
            order_list.save()

def shopping_car(request):
    return render(request, "order/shopping_car.html")