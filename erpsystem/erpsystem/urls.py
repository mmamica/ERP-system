"""erpsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from products_app import views
from order_app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls,name='admin'),
    url(r'^$',views.IndexView.as_view()),
    url(r'^product_app/',include('products_app.urls',namespace='products_app')),
    url(r'^order_app/',include('order_app.urls',namespace='order_app')),
    url(r'^admin_app/',include('admin_app.urls',namespace='admin_app')),
]
