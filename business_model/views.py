from django.shortcuts import render
from business_model.models import *

# Create your views here.
from django.views.generic import ListView, CreateView, DetailView

class ProductCreate(CreateView):
    model = Product
    fields = ['product_name','common_name','specification','price','medicare','product_factroy','symptoms','present_business']

class ProductDetail(DetailView):
    context_object_name = "product"
    queryset = Product.objects.all()