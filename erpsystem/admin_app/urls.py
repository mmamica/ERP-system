from django.conf.urls import url
from admin_app import views

app_name = 'admin_app'

urlpatterns = [
   url(r'^$',views.IndexView.as_view(),name='index'),
   url(r'^$',views.AdminCheckoutListView.as_view(),name='list'),
]
