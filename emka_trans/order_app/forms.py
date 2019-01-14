from django import forms
from order_app.models import OrderedProducts
from products_app.models import Product
from order_app.models import Checkout
from accounts.models import UserProfileInfo, User
import datetime


class OrderedProductsForm(forms.ModelForm):
    name = forms.ChoiceField(widget=forms.Select())
    iquery2=Product.objects.values_list('genre',flat=True).distinct()
    iquery_choices2 = [('', '')] + [(id, id) for id in iquery2]
    genre=forms.ChoiceField(choices=iquery_choices2, widget=forms.Select(attrs={'style': 'display:none;'}))

    class Meta():
        model=OrderedProducts
        fields=('name','genre','amount')

    # def clean(self):
    #     cd = self.cleaned_data
    #     cluster = UserProfileInfo.objects.get(user=self.user).id_cluster
    #     delivers = UserProfileInfo.objects.filter(id_cluster=cluster, is_client=False)
    #
    #     for deliver in delivers:
    #         check_product=Product.objects.filter(name=cd['name'], genre=cd['genre'],
    #                                                  name_deliver=deliver.user).count()
    #         if check_product!=0:
    #             prod=Product.objects.get(name=cd['name'], genre=cd['genre'], name_deliver=deliver.user)
    #
    #     if prod.amount<cd.get('amount'):
    #         self.add_error('amount','Niedostępna ilość produktu!')
    #
    #     return cd

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.CONSTANST=self.user
        self.ajax=kwargs.pop('ajax', True)
        super(OrderedProductsForm, self).__init__(*args, **kwargs)

        print(self.user)

        if not self.ajax:
            cluster = UserProfileInfo.objects.get(user=self.user).id_cluster
            delivers = UserProfileInfo.objects.filter(id_cluster=cluster, is_client=False)
            #deliver=delivers.user.username
            iquery=[]
            for deliver in delivers:
                name=deliver.user.username
                iquery = iquery + (list(Product.objects.filter(name_deliver=User.objects.get(username=name)).values_list('name',
                                                                                                     flat=True).distinct()))
            iquery=list(set(iquery))
            iquery_choices=[('', '')] + [(id, id) for id in iquery]
            self.fields['name'].choices = iquery_choices
        else:
            self.ajax=False
            iquery = Product.objects.values_list('name',flat=True).distinct()
            iquery_choices = [('', '')] + [(id, id) for id in iquery]
            self.fields['name'].choices = iquery_choices


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
            self.add_error('date', "The limit for this day is over.")

        elif(cd.get('date')<datetime.date.today()):
            self.add_error('date', "Choose future date.")

        elif(slots.count()>0):
            self.add_error('hour',"This slot is already taken.")

        return cd

    def __init__(self, *args, **kwargs):
        super(CheckoutCreateForm, self).__init__(*args, **kwargs)
        self.fields['hour'].label = "Preferred delivery hour"
        self.fields['date'].label = "Delivery date"

