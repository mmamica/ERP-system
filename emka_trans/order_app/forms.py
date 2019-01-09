from django import forms
from order_app.models import OrderedProducts
from products_app.models import Product
from order_app.models import Checkout
import datetime


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

    def clean(self):
        cd = self.cleaned_data
        prod = Product.objects.get(name=cd.get('name'), genre=cd.get('genre'))
        if prod.amount<cd.get('amount'):
            self.add_error('amount','Niedostępna ilość produktu!')

        return cd

class CheckoutCreateForm(forms.ModelForm):
    class Meta():
        model=Checkout
        fields=('date','hour')
        widgets = {'date': forms.DateInput(attrs={'id': 'datepicker'})}

    def clean(self):
        cd = self.cleaned_data
        chosen_date=cd.get('date')
        chosen_hour=cd.get('hour')
        checkouts=Checkout.objects.filter(date=chosen_date)
        slots=Checkout.objects.filter(date=chosen_date, hour=chosen_hour)
        times=checkouts.count()
        if (times>=3):
            self.add_error('date', "Wyczerpano limit zamówień na ten dzień!")

        elif(cd.get('date')<datetime.date.today()):
            self.add_error('date', "Wybierz przyszłą datę!")

        elif(slots.count()>0):
            self.add_error('hour',"Ten slot jest już zajety!")

        return cd

    def __init__(self, *args, **kwargs):
        super(CheckoutCreateForm, self).__init__(*args, **kwargs)
        self.fields['hour'].label = "Preferowana godzina"
        self.fields['date'].label = "Data dostarczenia"

