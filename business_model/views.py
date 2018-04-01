from django.shortcuts import render
from business_model.models import *

# Create your views here.
from django.views.generic import ListView, CreateView, DetailView

class ProductCreate(CreateView):
    model = Product
    fields = ['product_name','common_name','specification','price','medicare','product_factory','symptoms','present_business']

class ProductDetail(DetailView):
    context_object_name = "product"
    queryset = Product.objects.all()
    
class ProductList(ListView):
    model = Product
    cotext_object_name = 'all_products'
    
class BMCreate(CreateView):
    model = BusniessManager
    fields = ['bm_name', 'variety_name', 'phone', 'email', 'bank_account' ,'product_name',  'royalty_unit']
    
class BMDetail(DetailView):
    context_object_name = "bm"
    queryset = BusniessManager.objects.all()
    
class BMList(ListView):
    model = BusniessManager
    cotext_object_name = 'all_busniess_managers'

class CustomerCreate(CreateView):
    model = Customer
    fields = ['customer_name', 'variety_name', 'phone', 'email', 'bank_account' , 'product_name', 'academic_promotion_unit']
    
class CustomerDetail(DetailView):
    context_object_name = "Customer"
    queryset = Customer.objects.all()
    
class CustomerList(ListView):
    model = Customer
    cotext_object_name = 'all_customers'
    
