from django.contrib import admin
from order_app.models import Order,OrderedProducts,Checkout

# Register your models here.
admin.site.register(Order)
admin.site.register(OrderedProducts)
admin.site.register(Checkout)
