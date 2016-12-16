from django.db import models

# Create your models here.
class PositiveFloat(models.FloatField):
    def __init__(self, *args, **kwargs):
        super(PositiveFloat, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': 0.0}
        defaults.update(kwargs)
        return super(PositiveFloat, self).formfield(**defaults)

GOODS_TYPE = (('A', 'A'),
              ('B', 'B'),
              ('C', 'C'),
              ('D', 'D'),
              ('E', 'E'),)

class GoodsType(models.Model):

    type = models.CharField(choices=GOODS_TYPE, max_length=1)
    kilo = PositiveFloat(blank=True, default=0, null=True)

class GoodsPrice(models.Model):
    goods = models.CharField(choices=GOODS_TYPE, max_length=1)
    price = PositiveFloat(default=0)
    discount_num = models.PositiveIntegerField(default=0)
    discount_price = PositiveFloat(default=0)



