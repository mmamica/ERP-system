
from django.conf.urls import url
from order_app import views

app_name = 'order_app'

urlpatterns = [
    url(r'^$',views.CheckoutListView.as_view(),name='list'),
    url(r'^(?P<pk>\d+)/$',views.CheckoutDetailView.as_view(),name='detail'),
    url(r'^create/$',views.CheckoutCreateView.as_view(),name='create'),
    url(r'^update/(?P<pk>\d+)/$',views.CheckoutUpdateView.as_view(),name='update'),
    #url(r'^product/(?P<pk>\d+)/$',views.OrderedProductsDetailView.as_view(),name='product_detail'),
    url(r'^update_product/(?P<pk>\d+)/$',views.ProductUpdateView.as_view(),name='update_product'),
    url(r'^delete_order/(?P<pk>\d+)/$',views.CheckoutDeleteView.as_view(),name='delete'),
    url(r'^delete_product/(?P<pk>\d+)/$',views.ProductDeleteView.as_view(),name='delete_product'),
    url(r'^create/(?P<pk>\d+)/add_product$', views.ProductAddView.as_view(), name='add_product'),
    url(r'confirm/(?P<pk>\d+)',views.ConfirmCheckoutView.as_view(),name='confirm'),
    url(r'ajax/load_genres/', views.load_genres, name='ajax_load_genres'),
]