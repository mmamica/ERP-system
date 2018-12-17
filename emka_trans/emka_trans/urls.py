"""emka_trans URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from accounts import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    #url(r'^admin/',include('admin_app.urls'), name='admin'),
    url(r'^admin_app/',include('admin_app.urls',namespace='admin_app')),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^logout/$',views.LogoutView.as_view(), name='logout'),
    url(r'^user/',include('accounts.urls')),
    url(r'^orders/',include('order_app.urls'),name='order_app'),
    url(r'^products/',include('products_app.urls'), name='products_app'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
