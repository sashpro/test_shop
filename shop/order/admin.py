from django.contrib import admin
from .models import GoodsPrice
# Register your models here.

class GoodsPriceAdmin(admin.ModelAdmin):
    class Meta:
        model = GoodsPrice


admin.site.register(GoodsPrice, GoodsPriceAdmin)