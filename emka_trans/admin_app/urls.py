from django.conf.urls import url
from admin_app import views

app_name = 'admin_app'

urlpatterns = [
   url(r'^dashboard/$',views.IndexView.as_view(),name='index'),
   url(r'^dashboard1/$', views.IndexView1.as_view(), name='index1'),
   url(r'^dashboard2/$', views.IndexView2.as_view(), name='index2'),
   url(r'^dashboard3/$', views.IndexView3.as_view(), name='index3'),
   url(r'^dashboard20/$', views.IndexView20.as_view(), name='index20'),
   url(r'^dashboard21/$', views.IndexView21.as_view(), name='index21'),
   url(r'^dashboard22/$', views.IndexView22.as_view(), name='index22'),
   url(r'^dashboard23/$', views.IndexView23.as_view(), name='index23'),
   url(r'^orders/$',views.AdminCheckoutListView.as_view(),name='order_list'),
   url(r'^orders/(?P<pk>\d+)/$',views.AdminCheckoutDetailView.as_view(),name='order_detail'),
   url(r'^products/$',views.AdminProductListView.as_view(),name='product_list'),
   url(r'^runClarkeWright/$', views.runClarkeWright, name='runClarkeWright'),
    url(r'^runUpdate/$', views.runUpdate, name='runUpdate'),

]