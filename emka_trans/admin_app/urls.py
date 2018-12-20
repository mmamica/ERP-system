from django.conf.urls import url
from admin_app import views

app_name = 'admin_app'

urlpatterns = [
   url(r'^dashboard/$',views.IndexView.as_view(),name='index'),
   url(r'^orders/$',views.AdminCheckoutListView.as_view(),name='order_list'),
   url(r'^orders/(?P<pk>\d+)/$',views.AdminCheckoutDetailView.as_view(),name='order_detail'),
   url(r'^products/$',views.AdminProductListView.as_view(),name='product_list'),
]