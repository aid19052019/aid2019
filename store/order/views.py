from django.shortcuts import render
from . import models

# Create your views here.
def list(request):
    # user_id = request.GET.get("user_id")
    # order = models.Order.objects.all(user_id = user_id)
    # return render(request,"/order/order_list.html",locals())
    return render(request,"order/order.html")

