from django.shortcuts import render
from .forms import OrderForm
from .models import GoodsType
import json

# Create your views here.
def show_order(request):
    summary = 0
    if request.method == 'GET':
        form = OrderForm()
    elif request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            cart = GoodsType.objects.all()

            if cart is None:
                cart = GoodsType.objects.create()

            #cart.list.add(ad_custom)
            #cart.save()

    return render(request, 'order.html', {'form':form, 'sum': summary})


