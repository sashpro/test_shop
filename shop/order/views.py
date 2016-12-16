#-*- encoding: utf-8
from django.shortcuts import render
from .forms import OrderForm
from .models import GoodsType, GoodsPrice
from collections import defaultdict
from django.db.models import Count


def calculate(dict):
    """  discount “A costs 50 cents,”
    “three A cost $1.30,”
    “B costs 30 cents, two B cost 45 cents,”
    “$1.99 per kg of C,” and
    “D costs $1.20, E costs $0.90, buy two D, get one E free.”
    """
    gp = defaultdict(lambda: [0, 0, 0])
    obj = GoodsPrice.objects.all()

    for p in obj:
        gp[p.goods] = p.price, p.discount_num, p.discount_price
    summary = 0
    for goods in ('A', 'B', 'C', 'D'):
        if gp[goods][1] > 0:
            summary += dict[goods]/gp[goods][1]*gp[goods][2]+dict[goods] % gp[goods][1]*gp[goods][0]
        else:
            summary += dict[goods]*gp[goods][0]
    summary += (0 if (dict['E'] - dict['D']/2)<0 else dict['E'] - dict['D']/2)*gp['E'][0]
    return summary

# Create your views here.
def show_order(request):
    summary = 0
    cart = None
    dict = defaultdict(lambda: 0)
    cart = GoodsType.objects.all()
    if request.method == 'GET':
        form = OrderForm()
    elif request.method == 'POST':
        form = OrderForm(request.POST)
        if request.POST.get('delete', None):
            GoodsType.objects.all().delete()
        else:
            if form.is_valid():
                form.save()
                for t in cart:
                    dict[t.type] += t.kilo if (t.type in ['C']) else 1
                summary = calculate(dict)


    return render(request, 'order.html', {'form': form, 'cart': dict.items(), 'sum': summary})


