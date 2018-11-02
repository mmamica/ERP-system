from django.conf.urls import url
from products_app import views

app_name = 'products_app'

urlpatterns = [
    url(r'^$',views.ProductListView.as_view(),name='list'),
    url(r'^(?P<pk>\d+)/$',views.ProductDetailView.as_view(),name='detail'),
    url(r'^create/$',views.ProductCreateView.as_view(),name='create'),
    url(r'^update/(?P<pk>\d+)/$',views.ProductUpdateView.as_view(),name='update'),
    url(r'^delete/(?P<pk>\d+)/$',views.ProductDeleteView.as_view(),name='delete')
]
