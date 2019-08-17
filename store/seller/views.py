from django.shortcuts import render

# Create your views here.

def goods_store_view(request):
    if request.method == 'GET':
        return render(request,'seller/goods_store.html')