from django import forms
from .models import GoodsType

class OrderForm(forms.ModelForm):
    class Meta:
        model = GoodsType
        fields = ['type', 'kilo']



