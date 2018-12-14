from django import forms
from order_app.models import OrderedProducts
from products_app.models import Product

class OrderedProductsForm(forms.ModelForm):
    iquery=Product.objects.values_list('name',flat=True).distinct()
    iquery_choices=[('', '')] + [(id, id) for id in iquery]
    name=forms.ChoiceField(choices=iquery_choices, widget=forms.Select())
    iquery2=Product.objects.values_list('genre',flat=True).distinct()
    iquery_choices2 = [('', '')] + [(id, id) for id in iquery2]
    genre=forms.ChoiceField(choices=iquery_choices2, widget=forms.Select(attrs={'style': 'display:none;'}))

    class Meta():
        model=OrderedProducts
        fields=('name','genre','amount')
    #
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['genre'].widget = forms.HiddenInput()