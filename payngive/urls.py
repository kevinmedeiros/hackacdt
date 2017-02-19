"""payngive URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from core import views as views_core
from django.contrib.auth import views as auth_views
from rest_framework import routers
from api import views as views_payment

router = routers.DefaultRouter()
router.register(r'payment', views_payment.PaymentViewSet)

urlpatterns = [
    url(r'^registrar/$', views_core.register, name='register'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^$', views_core.home, name='home'),
    url(r'^dash/$', views_core.dash_a, name='dash'),
    url(r'^dash-b/$', views_core.dash_b, name='dashb'),
    url(r'^dash-c/$', views_core.dash_c, name='dashc'),
    url(r'^quemsomos/$', views_core.quemsomos, name='sobre'),
    url(r'^contato/$', views_core.contact, name='contact'),
    url(r'^admin/', admin.site.urls),
    url(r'^api-v01/payment/list$', views_payment.PaymentList.as_view()),
]
