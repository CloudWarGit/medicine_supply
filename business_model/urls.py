'''
Created on 2018年1月13日

@author: CloudWar
'''

from django.urls import path,re_path
from django.views.generic import TemplateView
from business_model.views import *
# from business_model.views import 

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html")),
    path('product/add/', ProductCreate.as_view(), name="product_add"),
    path('product/detail/(?P<pk>)?$', ProductDetail.as_view(), name='product-detail'),
    path('base/', TemplateView.as_view(template_name="base.html")),
    re_path('^pages/', TemplateView.as_view(template_name="pages/index.html")),
]