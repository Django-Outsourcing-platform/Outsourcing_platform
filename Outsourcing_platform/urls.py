"""Outsourcing_platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    # http://127.0.0.1:8000/admin
    url(r'^admin/', admin.site.urls),
    # http://127.0.0.1:8000/
    url(r'^', include('outsource.urls')),
    # http://127.0.0.1:8000/index/xxx
    # url(r'^index/', include('outsource.urls')),
    # http://127.0.0.1:8000/circle/xxx
    url(r'^circle/', include('circle.urls')),
    # http://127.0.0.1:8000/trade/xxx
    url(r'^trade/', include('trade.urls')),
    # http://127.0.0.1:8000/user/xxx
    url(r'^user/', include('user.urls')),
    # http://127.0.0.1:8000/payment/xxx
    url(r'^payment/', include('payment.urls')),
    # ckeditor设置admin页面
    url(r'^ckeditor', include('ckeditor_uploader.urls')),
]
