from django.db import models

# Create your models here.
class GoodsType(models.Model):
    GOODS_TYPE = (('A', 'A'),
                  ('B', 'B'),
                  ('C', 'C'),
                  ('D', 'D'),
                  ('E', 'E'),)

    type = models.CharField(choices=GOODS_TYPE, max_length=1)
    kilo = models.PositiveIntegerField(blank=True)


